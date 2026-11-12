

function [LT, LF, VF, NLF, NVF, FPE, FCE_L, FCE_V, FM, FMT] = ...
         MTForce(a, time, LMT, VMT, LT0, LF0, aV, Vmax, FM_max, PA, Max_LMT)

% a: Muscle activation
% LMT: Length of Musculotendon
% Max_LMT: Maximum of Length of Musculotendon
% MAMT: Moment Arm of Musculotendon
% LF: Length of Fasicle
% LT: Length of Tendon
% LT0: Tendon slack length
% LF0: Optimal fiber length
% aV: Coefficient
% Vmax: Muscle maximum shortening velocity
% PCSA: Physiological Cross-Sectional Area
% PA: Pennation Angle in rad
% FM_max: Maximum isometric muscle force


% Muscle maximal activation
Ku_max = 1;

% Tendon parameters (we do not apply tendon mechanics here)
KT1 = 0.1;
KT2 = 90;

% Muscle parallel elastic element parameters
KPE1 = 0.0075;
KPE2 = 11.6;


% Muscle and tendon visocity coefficients
bT = 0.02; % N.s/m
bM = 0.02; % N.s/m

% Computation of tendon and muscle length/normalized length 
PA = PA.*(pi/180); % deg to rad
LT = Max_LMT - 1.05*LF0*cos(PA);  
% LT = repmat(LT, size(LMT,1),1);
LF = (LMT-LT)./cos(PA);
NLF = LF./LF0;

% Note: Only here since the tendon length is constant we consider LT0 as LT
LT0 = mean(LT);
NLT = LT./LT0;


% Muscle force-length contractile element parameters 
if (LT0/LF0)<=1
  rho = 6;
else
  rho = 3;
end
betha = 1.55;
omega = 0.55;


% Computation of muscle (fasicle) velocity/normalized velocity
% dt = time(2)-time(1);
% for i=1:size(LF,1)
%  if i==1  
%    VF(i,1) = (-LF(i+2,1)+4*LF(i+1,1)-3*LF(i,1))/(2*dt);  
%  elseif (i>1) && (i<size(LF,1))
%    VF(i,1) = (LF(i+1,1)-LF(i-1,1))/(2*dt);  
%  else
%    VF(i,1) = (3*LF(i,1)-4*LF(i-1,1)+LF(i-2,1))/(2*dt);  
%  end  
% end
VF = VMT/cos(PA);
NVF = VF./abs(Vmax);

% For the whole range
% LF = 1.5*LF0*time/max(time)+0.2*LF0;
% NLF = LF./LF0;
% 
% VF = 2*Vmax*time/max(time)-Vmax;
% NVF = VF./abs(Vmax);



% FPE: force of muscle parallel elastic element
FPE = (KPE1/KPE2)*(exp(KPE2.*((LF./LF0)-1))-1);
FPE = FPE*0;

% FCE_L: Muscle force-length relationship
FCE_L = exp(-abs((NLF.^betha-1)./omega).^rho);


% FCE_V: Muscle force-velocity relationship
b0 = Vmax*0.8/(aV+1);
b1 = (1.8*(Vmax+b0)-b0)/Vmax;
for i=1:size(NVF,1)
    if NVF(i,1)>=0  
      FCE_V(i,1) = ((b0/Vmax) + b1*NVF(i,1))./((b0/Vmax) + NVF(i,1));
    else
      b = (aV/FM_max)*(Vmax);
      FCE_V(i,1) = ((FM_max*b-aV*VF(i,1))./(VF(i,1)+b))/FM_max;
     
    % FCE_V(i,1) = (1 + NVF(i,1))./(1 - aV*NVF(i,1)); % Table 10.3
    end
end


% FM: Muscle (fascicle) force
FM = FM_max.*(FCE_L.*FCE_V.*Ku_max.*a + FPE + bM.*VF);

% FMT: force of Musculotendon unit
FMT = FM.*cos(PA);

end


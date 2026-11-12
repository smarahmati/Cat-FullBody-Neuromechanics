

clear
clc
%
delete(gcp('nocreate'))
myCluster.NumWorkers = 8;
parpool('local',8)
%}

for numTrial = 1:68
    save('numTrial.mat', 'numTrial');


% Muscles
numTrialStr = [int2str(floor(numTrial/10)), int2str(mod(numTrial, 10))];
load(['MTLengthVelocityMomentArm_', numTrialStr, '.mat']);


MaxFunctionEvaluations_Data = 10^30;
MaxIterations_Data = 300;
OptimalityTolerance_Data = 10^-30;
StepTolerance_Data = 10^-30;
ObjectiveLimit_Data = 10^-30;
ConstraintTolerance_Data = 10^-30;


nti = size(MTLengthVelocityMomentArm{1, 1}.Length,1); % size of time iterations  
nm =  size(MTLengthVelocityMomentArm,1);              % number of muscles 


lb =  rand(1,nm)*0;
ub =  rand(1,nm)*0 + inf; 


tic;
for TS = 1:1:nti
TS 
save(['TS_', numTrialStr ,'.mat'],'TS');

    
%if TS>1; x0 = x; end
 x0 = rand(1,nm);

[x,fval,exitflag,output,lambda,grad,hessian] = IPGenerateCode(x0,lb,ub,MaxFunctionEvaluations_Data,MaxIterations_Data,OptimalityTolerance_Data,StepTolerance_Data,ObjectiveLimit_Data,ConstraintTolerance_Data);


% Activations(TS,:) = x; 
Total_Muscle_Fatigue(TS,1) = fval; 

%----- Activations -------------
for j=1:nm
Activations{j,1}.Name = MTLengthVelocityMomentArm{j, 1}.Name;
Activations{j,1}.a(TS,1) = x(j);
end


end

save(['Activations_', numTrialStr ,'.mat'], 'Activations');
save(['Total_Muscle_Fatigue_' numTrialStr ,'.mat'], 'Total_Muscle_Fatigue');

elapsed = toc

end

clear
clc

% This m-file makes a weighted average of muscle geometry parameters (a & phi)
% with respect to mean muscle moments

% MuscleForceMoment = load('MuscleForceMoment.mat');
% MuscleForceMoment = MuscleForceMoment.MuscleForceMoment;

CurrentMuscleMorphologicalParameters = load('CurrentMuscleMorphologicalParameters.mat');
CurrentMuscleMorphologicalParameters = CurrentMuscleMorphologicalParameters.CurrentMuscleMorphologicalParameters;

Cluster_Function = load('Cluster_Function.mat');
Cluster_Function = Cluster_Function.Cluster_Function;



% Rows related to considered muscles
RTM = [1,1 ; 2,2; 5,5 ; 6,7; 8,8; 9,9; 10,11; 14,15; 16,17; 18,19; 20,21; ...
      30,31 ; 32,33; 34,34; 35,36; 37,38; 39,40; 41,42; 43,44; 45,46; 47,48; ...
      49,50; 51,52; 53,54; 55,56; 57,58; 59,60; 61,62; 63,64; 65,66; 67,68; ...
      69,69; 70,70; 71,71; 72,72; 73,73; 74,74; 75,75; 76,76; 77,77]; 



%-----------Shoulder Extensors-------------------------------------------------------------------------------
G = 1;
MM = RTM(Cluster_Function{G},:); % MM i.e muscle morphologies
MN = unique(sort(MM(:)));        % MN i.e muscle number

for i=1:size(MN,1)
Muscle_Group{G,1}(i,:) = CurrentMuscleMorphologicalParameters{MN(i,1), 1}.Parameters;  
end
 
A = Muscle_Group{G,1}(:,5).R1; % joint radius
B = A(~isnan(A));

R1 = mean(B);
R1min = min(B);
R1max = max(B);

% Taken from Subscapularis (72)
% Taken from Supraspinatus (71)
% Taken from Teres Minor (77)
NineMuscleMorphParaInitial{G,1}.Name = 'Shoulder Extensors';
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters = CurrentMuscleMorphologicalParameters{72, 1}.Parameters;
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.R1 = R1;  

NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.MinR1 = R1min; 
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.MaxR1 = R1max; 




%-----------Elbow Extensors-------------------------------------------------------------------------------
G = 2;
MM = RTM(Cluster_Function{G},:); % MM i.e muscle morphologies
MN = unique(sort(MM(:)));        % MN i.e muscle number

for i=1:size(MN,1)
Muscle_Group{G,1}(i,:) = CurrentMuscleMorphologicalParameters{MN(i,1), 1}.Parameters;  
end
 
A = Muscle_Group{G,1}(:,5).R1;
B = A(~isnan(A));

R1 = mean(B);
R1min = min(B);
R1max = max(B);

% Taken from Anconeus (2)
% Taken from Epitrochlearis (34)
% Taken from Triceps Brachii Lateralis (74)
% Taken from Triceps Brachii Medial (76)
NineMuscleMorphParaInitial{G,1}.Name = 'Elbow Extensors';
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters = CurrentMuscleMorphologicalParameters{74, 1}.Parameters;
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.R1 = R1;  

NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.MinR1 = R1min; 
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.MaxR1 = R1max; 


%-----------BicepsBrachii-------------------------------------------------------------------------------
G = 3;
MM = RTM(Cluster_Function{G},:);   % MM i.e muscle morphologies
MN = unique(sort(MM(:)));          % MN i.e muscle number

for i=1:size(MN,1)
Muscle_Group{G,1}(i,:) = CurrentMuscleMorphologicalParameters{MN(i,1), 1}.Parameters;  
end

% Taken from Biceps Brachii
NineMuscleMorphParaInitial{G,1}.Name = 'Biceps Brachii';
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters = CurrentMuscleMorphologicalParameters{5, 1}.Parameters;



%-----------Elbow Flexors (Taken from Brachialis) -------------------------------------------------------------------------------
G = 4;
MM = RTM(Cluster_Function{G},:); % MM i.e muscle morphologies
MN = unique(sort(MM(:)));        % MN i.e muscle number

for i=1:size(MN,1)
Muscle_Group{G,1}(i,:) = CurrentMuscleMorphologicalParameters{MN(i,1), 1}.Parameters;  
end
 
A = Muscle_Group{G,1}(:,5).R1OW;
B = A(~isnan(A));

R1 = mean(B);
R1min = min(B);
R1max = max(B);

% Taken from Brachialis (8)
NineMuscleMorphParaInitial{G,1}.Name = 'Elbow Flexors';
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters = CurrentMuscleMorphologicalParameters{8, 1}.Parameters;
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.R1 = R1;  

NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.MinR1 = R1min; 
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.MaxR1 = R1max; 


%-----------Elbow Flexors (Taken from Brachioradialis) -------------------------------------------------------------------------------
G = 4;
MM = RTM(Cluster_Function{G},:); % MM i.e muscle morphologies
MN = unique(sort(MM(:)));        % MN i.e muscle number

for i=1:size(MN,1)
Muscle_Group{G,1}(i,:) = CurrentMuscleMorphologicalParameters{MN(i,1), 1}.Parameters;  
end
 
A = Muscle_Group{G,1}(:,5).R1OW;
B = A(~isnan(A));

R1WI = mean(B);
R1WImin = min(B);
R1WImax = max(B);


% Taken from Brachioradialis (6, 7)
NineMuscleMorphParaInitial{G,1}.Name = 'Elbow Flexors';
NineMuscleMorphParaInitial{G,1}.MorphologicalParametersVia.OW = CurrentMuscleMorphologicalParameters{6, 1}.Parameters;
NineMuscleMorphParaInitial{G,1}.MorphologicalParametersVia.WI = CurrentMuscleMorphologicalParameters{7, 1}.Parameters;
NineMuscleMorphParaInitial{G,1}.MorphologicalParametersVia.WI.R1WI = R1WI;  

NineMuscleMorphParaInitial{G,1}.MorphologicalParametersVia.WI.MinR1WI = R1WImin; 
NineMuscleMorphParaInitial{G,1}.MorphologicalParametersVia.WI.MaxR1WI = R1WImax; 


%-----------Elbow Flexors Wrist Flexors-------------------------------------------------------------------------------
G = 5;
MM = RTM(Cluster_Function{G},:); % MM i.e muscle morphologies
MN = unique(sort(MM(:)));                % MN i.e muscle number

for i=1:size(MN,1)
Muscle_Group{G,1}(i,:) = CurrentMuscleMorphologicalParameters{MN(i,1), 1}.Parameters;  
end
 
R1OW = (Muscle_Group{G,1}(:,5).R1OW(1) + Muscle_Group{G,1}(:,5).R1OW(3) + Muscle_Group{G,1}(:,5).R1OW(5) + ...
        Muscle_Group{G,1}(:,5).R1OW(7) + Muscle_Group{G,1}(:,5).R1OW(9))/5;

R1WI = (Muscle_Group{G,1}(:,6).R2OW(1) + Muscle_Group{G,1}(:,5).R1OW(4) + Muscle_Group{G,1}(:,5).R1OW(6) + ...
        Muscle_Group{G,1}(:,5).R1OW(8) + Muscle_Group{G,1}(:,5).R1OW(10))/5;


R1OWmin = min([ Muscle_Group{G,1}(:,5).R1OW(1) , Muscle_Group{G,1}(:,5).R1OW(3) , Muscle_Group{G,1}(:,5).R1OW(5) , ...
                Muscle_Group{G,1}(:,5).R1OW(7) , Muscle_Group{G,1}(:,5).R1OW(9)]);

R1OWmax = max([ Muscle_Group{G,1}(:,5).R1OW(1) , Muscle_Group{G,1}(:,5).R1OW(3) , Muscle_Group{G,1}(:,5).R1OW(5) , ...
                Muscle_Group{G,1}(:,5).R1OW(7) , Muscle_Group{G,1}(:,5).R1OW(9)]);


R1WImin = min([Muscle_Group{G,1}(:,6).R2OW(1) , Muscle_Group{G,1}(:,5).R1OW(4) , Muscle_Group{G,1}(:,5).R1OW(6) , ...
               Muscle_Group{G,1}(:,5).R1OW(8) , Muscle_Group{G,1}(:,5).R1OW(10)]);

R1WImax = max([Muscle_Group{G,1}(:,6).R2OW(1) , Muscle_Group{G,1}(:,5).R1OW(4) , Muscle_Group{G,1}(:,5).R1OW(6) , ...
               Muscle_Group{G,1}(:,5).R1OW(8) , Muscle_Group{G,1}(:,5).R1OW(10)]);


% Taken from Extensor digitorum communis 2
NineMuscleMorphParaInitial{G,1}.Name = 'Elbow Flexors Wrist Flexors';
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.OW = CurrentMuscleMorphologicalParameters{14, 1}.Parameters;
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.WI = CurrentMuscleMorphologicalParameters{15, 1}.Parameters;
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.OW.R1OW = R1OW;  
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.WI.R1WI = R1WI;  


NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.OW.MinR1OW = R1OWmin; 
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.OW.MaxR1OW = R1OWmax; 

NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.WI.MinR1WI = R1WImin; 
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.WI.MaxR1WI = R1WImax; 


%-----------Wrist Flexors-------------------------------------------------------------------------------
G = 6;

MM = RTM(Cluster_Function{G},:); % MM i.e muscle morphologies
MN = unique(sort(MM(:)));                % MN i.e muscle number

for i=1:size(MN,1)
Muscle_Group{G,1}(i,:) = CurrentMuscleMorphologicalParameters{MN(i,1), 1}.Parameters;  
end
 
A = Muscle_Group{G,1}(:,5).R1OW;
B = A(~isnan(A));

R1WI = mean(B);
R1WImin = min(B);
R1WImax = max(B);

% Taken from Extensor Pollicis Longus 1
NineMuscleMorphParaInitial{G,1}.Name = 'Wrist Flexors';
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.OW = CurrentMuscleMorphologicalParameters{30, 1}.Parameters;
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.WI = CurrentMuscleMorphologicalParameters{31, 1}.Parameters;
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.WI.R1WI = R1WI;  

NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.WI.MinR1WI = R1WImin; 
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.WI.MaxR1WI = R1WImax; 


%-----------Wrist Extensors-------------------------------------------------------------------------------
G = 7;
% Group a: Flexor Carpi Radialis(15), Flexor Carpi Ulnaris(16), 
% Flexor Digitorum Profundus(17-21), Palmaris Longus(27-31)
% Ga = [15; 16; 17; 18; 19; 20; 21; 27; 28; 29; 30; 31];
% Group b: Flexor Digitorum Superficialis(22-25)
% Gb = [22; 23; 24; 25];

MM = RTM(Cluster_Function{G},:); % MM i.e muscle morphologies
MN = unique(sort(MM(:)));                % MN i.e muscle number

for i=1:size(MN,1)
Muscle_Group{G,1}(i,:) = CurrentMuscleMorphologicalParameters{MN(i,1), 1}.Parameters;  
end
 
A = Muscle_Group{G,1}(:,5).R1OW;
B = A(~isnan(A));

R1WI = mean(B);
R1WImin = min(B);
R1WImax = max(B);

% Taken from Flexor digitorum profundus 1 (39, 40)
% Taken from Palmaris Longus 1 (59, 60)
NineMuscleMorphParaInitial{G,1}.Name = 'Wrist Extensors';
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.OW = CurrentMuscleMorphologicalParameters{39, 1}.Parameters;
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.WI = CurrentMuscleMorphologicalParameters{40, 1}.Parameters;
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.WI.R1WI = R1WI;  

NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.WI.MinR1WI = R1WImin; 
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.WI.MaxR1WI = R1WImax; 

%-----------Shoulder Flexors-------------------------------------------------------------------------------
G = 8;
MM = RTM(Cluster_Function{G},:); % MM i.e muscle morphologies
MN = unique(sort(MM(:)));        % MN i.e muscle number

for i=1:size(MN,1)
Muscle_Group{G,1}(i,:) = CurrentMuscleMorphologicalParameters{MN(i,1), 1}.Parameters;  
end
 
A = Muscle_Group{G,1}(:,5).R1;
B = A(~isnan(A));

R1 = mean(B);
R1min = min(B);
R1max = max(B);

% Taken from Teres Major
NineMuscleMorphParaInitial{G,1}.Name = 'Shoulder Extensors';
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters = CurrentMuscleMorphologicalParameters{73, 1}.Parameters;
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.R1 = R1;  


NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.MinR1 = R1min; 
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters.MaxR1 = R1max; 


%-----------Triceps Brachii Long-------------------------------------------------------------------------------
G = 9;
MM = RTM(Cluster_Function{G},:);   % MM i.e muscle morphologies
MN = unique(sort(MM(:)));          % MN i.e muscle number

for i=1:size(MN,1)
Muscle_Group{G,1}(i,:) = CurrentMuscleMorphologicalParameters{MN(i,1), 1}.Parameters;  
end

% Taken from Biceps Brachii
NineMuscleMorphParaInitial{G,1}.Name = 'Triceps Brachii Long';
NineMuscleMorphParaInitial{G,1}.MorphologicalParameters = CurrentMuscleMorphologicalParameters{75, 1}.Parameters;



save('NineMuscleMorphParaInitial.mat','NineMuscleMorphParaInitial');

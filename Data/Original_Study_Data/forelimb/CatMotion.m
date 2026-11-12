clear
clc



%% Cat's info
[~,sheets_info] = xlsfinfo('7CatsRevised.xlsx');

for i = 1:numel(sheets_info)         
 TInfo{i,1}.Data = readtable('7CatsRevised.xlsx','Sheet',char(sheets_info(i)),'Format','auto','PreserveVariableNames',true);
 TInfo{i,1}.SheetName = sheets_info{i};
end


%% Cat's motion data
[~,sheets_motion] = xlsfinfo('BredCatsDataForeLimbs3Revised.xls');

for i = 1:numel(sheets_motion)    
%     [num,headers,raw] = xlsread('4cats_level_fore6.xls',i);
%     Tm{i,1}.Data = num;
%     Tm{i,1}.Headers = headers;
%     Tm{i,1}.SheetName = sheets_motion{i};
        
    TMot{i,1}.Data = readtable('BredCatsDataForeLimbs3Revised.xls','Sheet',char(sheets_motion(i)),'Format','auto','PreserveVariableNames',true);
    TMot{i,1}.SheetName = sheets_motion{i};
end


%% Cat's forelimb length and orientation data
[~,sheets_motion2] = xlsfinfo('CatsDataForeLimbs8_AddedForelimbLengthOrientation.xls');

k = 0;
for i = numel(sheets_motion2)-1:numel(sheets_motion2)   
 k = k+1;
 TMot{numel(sheets_motion)+k,1}.Data = readtable('CatsDataForeLimbs8_AddedForelimbLengthOrientation.xls','Sheet',char(sheets_motion2(i)),'Format','auto','PreserveVariableNames',true);
 TMot{numel(sheets_motion)+k,1}.SheetName = sheets_motion2{i};
end

T2C1 = table2cell(TMot{end-1, 1}.Data);
T2C2 = table2cell(TMot{end, 1}.Data);
T2C1t = T2C1';
T2C2t = T2C2';

for i=1:size(T2C1t,2)
T2C1t{1,i} = strcat(string(T2C1t(1,i)),'_',num2str(i));
T2C2t{1,i} = strcat(string(T2C2t(1,i)),'_',num2str(i));
end

Tab1 = cell2table(T2C1t(2:end,:),"VariableNames",string(T2C1t(1,:)));
Tab2 = cell2table(T2C2t(2:end,:),"VariableNames",string(T2C2t(1,:)));

TMot{end-1,1}.Data = Tab1;
TMot{end,1}.Data = Tab2;

g = 9.806; % N/s^2


%% Cat's Information
%------------------------- Anthropometric data (TInfo{2,1})-------------------------------------
Sheet = TInfo{2, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
for i=1:size(Sheet.Data,1)  
CatName = Sheet.Data.(VariableNames{1}){i};

MotionData.Cases.MLW.Mass.(CatName) = Sheet.Data.(VariableNames{2})(i);                % kg
MotionData.Cases.MLW.ScapulaLength.(CatName) = Sheet.Data.(VariableNames{3})(i);       % m
MotionData.Cases.MLW.UpperArmLength.(CatName) = Sheet.Data.(VariableNames{4})(i);      % m
MotionData.Cases.MLW.ForeArmLength.(CatName) = Sheet.Data.(VariableNames{5})(i);       % m
MotionData.Cases.MLW.CarpalsLength.(CatName) = Sheet.Data.(VariableNames{6})(i);       % m
MotionData.Cases.MLW.ForeDigitsLength.(CatName) = Sheet.Data.(VariableNames{7})(i);    % m
MotionData.Cases.MLW.ThighLength.(CatName) = Sheet.Data.(VariableNames{8})(i);         % m
MotionData.Cases.MLW.ShankLength.(CatName) = Sheet.Data.(VariableNames{9})(i);         % m
MotionData.Cases.MLW.TarsalsLength.(CatName) = Sheet.Data.(VariableNames{10})(i);      % m
MotionData.Cases.MLW.HindDigitsLength.(CatName) = Sheet.Data.(VariableNames{11})(i);   % m

MotionData.Cases.MLW.ForeLimbLength.(CatName) = MotionData.Cases.MLW.ScapulaLength.(CatName)+ ...
                                                MotionData.Cases.MLW.UpperArmLength.(CatName)+...
                                                MotionData.Cases.MLW.ForeArmLength.(CatName)+...
                                                MotionData.Cases.MLW.CarpalsLength.(CatName); % m
                                         
MotionData.Cases.MLW.WeightInForeLimbLength.(CatName) = MotionData.Cases.MLW.Mass.(CatName)*g*...
                                                        MotionData.Cases.MLW.ForeLimbLength.(CatName); % Nm    
                                                 
                                                 
MotionData.Cases.MLW.HindLimbLength.(CatName) = MotionData.Cases.MLW.ThighLength.(CatName)+ ...
                                                MotionData.Cases.MLW.ShankLength.(CatName)+...
                                                MotionData.Cases.MLW.TarsalsLength.(CatName); % m
                                         
MotionData.Cases.MLW.WeightInHindLimbLength.(CatName) = MotionData.Cases.MLW.Mass.(CatName)*g*...
                                                        MotionData.Cases.MLW.HindLimbLength.(CatName); % Nm  
end

str = ["field = MotionData.Cases.MLW.Var";
       "VarVector = cellfun(@(x)(field.(x)),fieldnames(field))";
       "VarVector = VarVector(~isnan(VarVector))";
       "MotionData.GenericCat.MLW.Var = mean(VarVector)"]; 
   
% create data for generic cat
Variables = {'Mass'; 'ScapulaLength'; 'UpperArmLength'; 'ForeArmLength'; ...
             'CarpalsLength'; 'ForeDigitsLength'; 'ThighLength'; 'ShankLength'; ...
             'TarsalsLength'; 'HindDigitsLength'; 'ForeLimbLength'; 'WeightInForeLimbLength'; ...
             'HindLimbLength'; 'WeightInHindLimbLength'};
         
for i=1:size(Variables,1)     
str2 = replace(str,'Var', Variables{i});
eval(str2{1});
eval(str2{2});
eval(str2{3});
eval(str2{4});
end


%------------------------- Center Of Mass data (TInfo{3,1})-------------------------------------
Sheet = TInfo{3, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
for i=1:size(Sheet.Data,1)  
CatName = Sheet.Data.(VariableNames{1}){i};

MotionData.Cases.SegmentCOM.Scapula.(CatName) = Sheet.Data.(VariableNames{2})(i);     % m
MotionData.Cases.SegmentCOM.UpperArm.(CatName) = Sheet.Data.(VariableNames{3})(i);    % m
MotionData.Cases.SegmentCOM.ForeArm.(CatName) = Sheet.Data.(VariableNames{4})(i);     % m
MotionData.Cases.SegmentCOM.Carpals.(CatName) = Sheet.Data.(VariableNames{5})(i);     % m
MotionData.Cases.SegmentCOM.ForeDigits.(CatName) = Sheet.Data.(VariableNames{6})(i);  % m
MotionData.Cases.SegmentCOM.Thigh.(CatName) = Sheet.Data.(VariableNames{7})(i);       % m
MotionData.Cases.SegmentCOM.Shank.(CatName) = Sheet.Data.(VariableNames{8})(i);       % m
MotionData.Cases.SegmentCOM.Tarsals.(CatName) = Sheet.Data.(VariableNames{9})(i);     % m
MotionData.Cases.SegmentCOM.HindDigits.(CatName) = Sheet.Data.(VariableNames{10})(i); % m
end

str = ["field = MotionData.Cases.SegmentCOM.Var";
       "VarVector = cellfun(@(x)(field.(x)),fieldnames(field))";
       "VarVector = VarVector(~isnan(VarVector))";
       "MotionData.GenericCat.SegmentCOM.Var = mean(VarVector)"]; 
      
% create data for generic cat
Variables = {'Scapula'; 'UpperArm'; 'ForeArm'; ...
             'Carpals'; 'ForeDigits'; 'Thigh'; ...
             'Shank'; 'Tarsals'; 'HindDigits'};
for i=1:size(Variables,1)     
str2 = replace(str,'Var', Variables{i});
eval(str2{1});
eval(str2{2});
eval(str2{3});
eval(str2{4});
end



%------------------------- Segment Mass (TInfo{4,1})-------------------------------------
Sheet = TInfo{4, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
for i=1:size(Sheet.Data,1)  
CatName = Sheet.Data.(VariableNames{1}){i};

MotionData.Cases.SegmentMass.Scapula.(CatName) = Sheet.Data.(VariableNames{2})(i);      % kg
MotionData.Cases.SegmentMass.UpperArm.(CatName) = Sheet.Data.(VariableNames{3})(i);     % kg
MotionData.Cases.SegmentMass.ForeArm.(CatName) = Sheet.Data.(VariableNames{4})(i);      % kg
MotionData.Cases.SegmentMass.Carpals.(CatName) = Sheet.Data.(VariableNames{5})(i);      % kg
MotionData.Cases.SegmentMass.ForeDigits.(CatName) = Sheet.Data.(VariableNames{6})(i);   % kg
MotionData.Cases.SegmentMass.Thigh.(CatName) = Sheet.Data.(VariableNames{7})(i);        % kg
MotionData.Cases.SegmentMass.Shank.(CatName) = Sheet.Data.(VariableNames{8})(i);        % kg
MotionData.Cases.SegmentMass.Tarsals.(CatName) = Sheet.Data.(VariableNames{9})(i);      % kg
MotionData.Cases.SegmentMass.HindDigits.(CatName) = Sheet.Data.(VariableNames{10})(i);  % kg
MotionData.Cases.SegmentMass.HeadNeck.(CatName) = Sheet.Data.(VariableNames{11})(i);    % kg
MotionData.Cases.SegmentMass.Trunk.(CatName) = Sheet.Data.(VariableNames{12})(i);       % kg

end
str = ["field = MotionData.Cases.SegmentMass.Var";
       "VarVector = cellfun(@(x)(field.(x)),fieldnames(field))";
       "VarVector = VarVector(~isnan(VarVector))";
       "MotionData.GenericCat.SegmentMass.Var = mean(VarVector)"]; 
   
% create data for generic cat
Variables = {'Scapula'; 'UpperArm'; 'ForeArm'; ...
             'Carpals'; 'ForeDigits'; 'Thigh'; ...
             'Shank'; 'Tarsals'; 'HindDigits';...
             'HeadNeck'; 'Trunk'};
for i=1:size(Variables,1)     
str2 = replace(str,'Var', Variables{i});
eval(str2{1});
eval(str2{2});
eval(str2{3});
eval(str2{4});
end



%------------------------- Moment Of Inertia (TInfo{5,1})-------------------------------------
Sheet = TInfo{5, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
for i=1:size(Sheet.Data,1)  
CatName = Sheet.Data.(VariableNames{1}){i};

MotionData.Cases.SegmentMOI.Scapula.(CatName) = Sheet.Data.(VariableNames{2})(i);      % kg.m^2
MotionData.Cases.SegmentMOI.UpperArm.(CatName) = Sheet.Data.(VariableNames{3})(i);     % kg.m^2
MotionData.Cases.SegmentMOI.ForeArm.(CatName) = Sheet.Data.(VariableNames{4})(i);      % kg.m^2
MotionData.Cases.SegmentMOI.Carpals.(CatName) = Sheet.Data.(VariableNames{5})(i);      % kg.m^2
MotionData.Cases.SegmentMOI.ForeDigits.(CatName) = Sheet.Data.(VariableNames{6})(i);   % kg.m^2
MotionData.Cases.SegmentMOI.Thigh.(CatName) = Sheet.Data.(VariableNames{7})(i);        % kg.m^2
MotionData.Cases.SegmentMOI.Shank.(CatName) = Sheet.Data.(VariableNames{8})(i);        % kg.m^2
MotionData.Cases.SegmentMOI.Tarsals.(CatName) = Sheet.Data.(VariableNames{9})(i);      % kg.m^2
MotionData.Cases.SegmentMOI.HindDigits.(CatName) = Sheet.Data.(VariableNames{10})(i);  % kg.m^2

end
str = ["field = MotionData.Cases.SegmentMOI.Var";
       "VarVector = cellfun(@(x)(field.(x)),fieldnames(field))";
       "VarVector = VarVector(~isnan(VarVector))";
       "MotionData.GenericCat.SegmentMOI.Var = mean(VarVector)"]; 
   
% create data for generic cat
Variables = {'Scapula'; 'UpperArm'; 'ForeArm'; ...
             'Carpals'; 'ForeDigits'; 'Thigh'; ...
             'Shank'; 'Tarsals'; 'HindDigits'};
         
for i=1:size(Variables,1)     
str2 = replace(str,'Var', Variables{i});
eval(str2{1});
eval(str2{2});
eval(str2{3});
eval(str2{4});
end



%------------------------- Number O fCycles (TInfo{6,1})-------------------------------------
Sheet = TInfo{6, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
for i=1:size(Sheet.Data,1)  
CatName = Sheet.Data.(VariableNames{1}){i};

MotionData.Cases.NumberOfCycles.Fx.(CatName) = Sheet.Data.(VariableNames{2})(i);             % dimensionless
MotionData.Cases.NumberOfCycles.Fz.(CatName) = Sheet.Data.(VariableNames{3})(i);             % dimensionless
MotionData.Cases.NumberOfCycles.MomentMC.(CatName) = Sheet.Data.(VariableNames{4})(i);       % dimensionless
MotionData.Cases.NumberOfCycles.MomentWrist.(CatName) = Sheet.Data.(VariableNames{5})(i);    % dimensionless
MotionData.Cases.NumberOfCycles.MomentElbow.(CatName) = Sheet.Data.(VariableNames{6})(i);    % dimensionless
MotionData.Cases.NumberOfCycles.MomentShoulder.(CatName) = Sheet.Data.(VariableNames{7})(i); % dimensionless
MotionData.Cases.NumberOfCycles.AngleMC.(CatName) = Sheet.Data.(VariableNames{8})(i);        % dimensionless
MotionData.Cases.NumberOfCycles.AngleWrist.(CatName) = Sheet.Data.(VariableNames{9})(i);     % dimensionless
MotionData.Cases.NumberOfCycles.AngleElbow.(CatName) = Sheet.Data.(VariableNames{10})(i);    % dimensionless
MotionData.Cases.NumberOfCycles.AngleShoulder.(CatName) = Sheet.Data.(VariableNames{11})(i); % dimensionless
MotionData.Cases.NumberOfCycles.XLeftShoulder.(CatName) = Sheet.Data.(VariableNames{12})(i); % dimensionless
MotionData.Cases.NumberOfCycles.XRightShoulder.(CatName) = Sheet.Data.(VariableNames{13})(i);% dimensionless
MotionData.Cases.NumberOfCycles.YLeftShoulder.(CatName) = Sheet.Data.(VariableNames{14})(i); % dimensionless
MotionData.Cases.NumberOfCycles.YRightShoulder.(CatName) = Sheet.Data.(VariableNames{15})(i);% dimensionless
MotionData.Cases.NumberOfCycles.VAMC.(CatName) = Sheet.Data.(VariableNames{16})(i);          % dimensionless
MotionData.Cases.NumberOfCycles.VAWrist.(CatName) = Sheet.Data.(VariableNames{17})(i);       % dimensionless
MotionData.Cases.NumberOfCycles.VAElbow.(CatName) = Sheet.Data.(VariableNames{18})(i);       % dimensionless
MotionData.Cases.NumberOfCycles.VAShoulder.(CatName) = Sheet.Data.(VariableNames{19})(i);    % dimensionless
MotionData.Cases.NumberOfCycles.PhiScap.(CatName) = Sheet.Data.(VariableNames{20})(i);       % dimensionless
MotionData.Cases.NumberOfCycles.VAPhiScap.(CatName) = Sheet.Data.(VariableNames{21})(i);     % dimensionless
MotionData.Cases.NumberOfCycles.ForeLimbLength.(CatName) = Sheet.Data.(VariableNames{22})(i);     % dimensionless
MotionData.Cases.NumberOfCycles.ForeLimbOrientation.(CatName) = Sheet.Data.(VariableNames{23})(i);     % dimensionless

end
str = ["field = MotionData.Cases.NumberOfCycles.Var";
       "VarVector = cellfun(@(x)(field.(x)),fieldnames(field))";
       "VarVector = VarVector(~isnan(VarVector))";
       "MotionData.GenericCat.NumberOfCycles.Var = mean(VarVector)"]; 
   
% create data for generic cat
Variables = {'Fx'; 'Fz'; 'MomentMC'; 'MomentWrist'; 'MomentElbow'; ...
             'MomentShoulder'; 'AngleMC'; 'AngleWrist'; 'AngleElbow'; 'AngleShoulder'; ...
             'XLeftShoulder'; 'XRightShoulder'; 'YLeftShoulder'; 'YRightShoulder'; ...
             'VAMC'; 'VAWrist'; 'VAElbow'; 'VAShoulder'; 'PhiScap'; 'VAPhiScap'};
         
for i=1:size(Variables,1)     
str2 = replace(str,'Var', Variables{i});
eval(str2{1});
eval(str2{2});
eval(str2{3});
eval(str2{4});
end
sum = 0;
for i=1:size(Variables,1)
sum = sum + MotionData.GenericCat.NumberOfCycles.(Variables{i}); 
end
MotionData.GenericCat.NumberOfCycles.Average = sum/size(Variables,1);



%------------------------- Cycel Time (TInfo{7,1})-------------------------------------
Sheet = TInfo{7, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
for i=1:size(Sheet.Data,1)  
CatName = Sheet.Data.(VariableNames{1}){i};

MotionData.Cases.CycleTime.Fx.(CatName) = Sheet.Data.(VariableNames{2})(i);             % s
MotionData.Cases.CycleTime.Fz.(CatName) = Sheet.Data.(VariableNames{3})(i);             % s
MotionData.Cases.CycleTime.MomentMC.(CatName) = Sheet.Data.(VariableNames{4})(i);       % s
MotionData.Cases.CycleTime.MomentWrist.(CatName) = Sheet.Data.(VariableNames{5})(i);    % s
MotionData.Cases.CycleTime.MomentElbow.(CatName) = Sheet.Data.(VariableNames{6})(i);    % s
MotionData.Cases.CycleTime.MomentShoulder.(CatName) = Sheet.Data.(VariableNames{7})(i); % s
MotionData.Cases.CycleTime.AngleMC.(CatName) = Sheet.Data.(VariableNames{8})(i);        % s
MotionData.Cases.CycleTime.AngleWrist.(CatName) = Sheet.Data.(VariableNames{9})(i);     % s
MotionData.Cases.CycleTime.AngleElbow.(CatName) = Sheet.Data.(VariableNames{10})(i);    % s
MotionData.Cases.CycleTime.AngleShoulder.(CatName) = Sheet.Data.(VariableNames{11})(i); % s
MotionData.Cases.CycleTime.XLeftShoulder.(CatName) = Sheet.Data.(VariableNames{12})(i); % s
MotionData.Cases.CycleTime.XRightShoulder.(CatName) = Sheet.Data.(VariableNames{13})(i);% s
MotionData.Cases.CycleTime.YLeftShoulder.(CatName) = Sheet.Data.(VariableNames{14})(i); % s
MotionData.Cases.CycleTime.YRightShoulder.(CatName) = Sheet.Data.(VariableNames{15})(i);% s
MotionData.Cases.CycleTime.VAMC.(CatName) = Sheet.Data.(VariableNames{16})(i);          % s
MotionData.Cases.CycleTime.VAWrist.(CatName) = Sheet.Data.(VariableNames{17})(i);       % s
MotionData.Cases.CycleTime.VAElbow.(CatName) = Sheet.Data.(VariableNames{18})(i);       % s
MotionData.Cases.CycleTime.VAShoulder.(CatName) = Sheet.Data.(VariableNames{19})(i);    % s
MotionData.Cases.CycleTime.PhiScap.(CatName) = Sheet.Data.(VariableNames{20})(i);       % s
MotionData.Cases.CycleTime.VAPhiScap.(CatName) = Sheet.Data.(VariableNames{21})(i);     % s

end
str = ["field = MotionData.Cases.CycleTime.Var";
       "VarVector = cellfun(@(x)(field.(x)),fieldnames(field))";
       "VarVector = VarVector(~isnan(VarVector))";
       "MotionData.GenericCat.CycleTime.Var = mean(VarVector)"]; 
   
% create data for generic cat
Variables = {'Fx'; 'Fz'; 'MomentMC'; 'MomentWrist'; 'MomentElbow'; ...
             'MomentShoulder'; 'AngleMC'; 'AngleWrist'; 'AngleElbow'; 'AngleShoulder'; ...
             'XLeftShoulder'; 'XRightShoulder'; 'YLeftShoulder'; 'YRightShoulder'; ...
             'VAMC'; 'VAWrist'; 'VAElbow'; 'VAShoulder'; 'PhiScap'; 'VAPhiScap'};
         
for i=1:size(Variables,1)     
str2 = replace(str,'Var', Variables{i});
eval(str2{1});
eval(str2{2});
eval(str2{3});
eval(str2{4});
end
sum = 0;
for i=1:size(Variables,1)
sum = sum + MotionData.GenericCat.CycleTime.(Variables{i}); 
end
MotionData.GenericCat.CycleTime.Average = sum/size(Variables,1);



%------------------------- Duty Factor (TInfo{8,1})-------------------------------------
Sheet = TInfo{8, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
for i=1:size(Sheet.Data,1)  
CatName = Sheet.Data.(VariableNames{1}){i};

MotionData.Cases.DutyFactor.Fx.(CatName) = Sheet.Data.(VariableNames{2})(i);             % dimensionless
MotionData.Cases.DutyFactor.Fz.(CatName) = Sheet.Data.(VariableNames{3})(i);             % dimensionless
MotionData.Cases.DutyFactor.MomentMC.(CatName) = Sheet.Data.(VariableNames{4})(i);       % dimensionless
MotionData.Cases.DutyFactor.MomentWrist.(CatName) = Sheet.Data.(VariableNames{5})(i);    % dimensionless
MotionData.Cases.DutyFactor.MomentElbow.(CatName) = Sheet.Data.(VariableNames{6})(i);    % dimensionless
MotionData.Cases.DutyFactor.MomentShoulder.(CatName) = Sheet.Data.(VariableNames{7})(i); % dimensionless
MotionData.Cases.DutyFactor.AngleMC.(CatName) = Sheet.Data.(VariableNames{8})(i);        % dimensionless
MotionData.Cases.DutyFactor.AngleWrist.(CatName) = Sheet.Data.(VariableNames{9})(i);     % dimensionless
MotionData.Cases.DutyFactor.AngleElbow.(CatName) = Sheet.Data.(VariableNames{10})(i);    % dimensionless
MotionData.Cases.DutyFactor.AngleShoulder.(CatName) = Sheet.Data.(VariableNames{11})(i); % dimensionless
MotionData.Cases.DutyFactor.XLeftShoulder.(CatName) = Sheet.Data.(VariableNames{12})(i); % dimensionless
MotionData.Cases.DutyFactor.XRightShoulder.(CatName) = Sheet.Data.(VariableNames{13})(i);% dimensionless
MotionData.Cases.DutyFactor.YLeftShoulder.(CatName) = Sheet.Data.(VariableNames{14})(i); % dimensionless
MotionData.Cases.DutyFactor.YRightShoulder.(CatName) = Sheet.Data.(VariableNames{15})(i);% dimensionless
MotionData.Cases.DutyFactor.VAMC.(CatName) = Sheet.Data.(VariableNames{16})(i);          % dimensionless
MotionData.Cases.DutyFactor.VAWrist.(CatName) = Sheet.Data.(VariableNames{17})(i);       % dimensionless
MotionData.Cases.DutyFactor.VAElbow.(CatName) = Sheet.Data.(VariableNames{18})(i);       % dimensionless
MotionData.Cases.DutyFactor.VAShoulder.(CatName) = Sheet.Data.(VariableNames{19})(i);    % dimensionless
MotionData.Cases.DutyFactor.PhiScap.(CatName) = Sheet.Data.(VariableNames{20})(i);       % dimensionless
MotionData.Cases.DutyFactor.VAPhiScap.(CatName) = Sheet.Data.(VariableNames{21})(i);     % dimensionless

end
str = ["field = MotionData.Cases.DutyFactor.Var";
       "VarVector = cellfun(@(x)(field.(x)),fieldnames(field))";
       "VarVector = VarVector(~isnan(VarVector))";
       "MotionData.GenericCat.DutyFactor.Var = mean(VarVector)"]; 
   
% create data for generic cat
Variables = {'Fx'; 'Fz'; 'MomentMC'; 'MomentWrist'; 'MomentElbow'; ...
             'MomentShoulder'; 'AngleMC'; 'AngleWrist'; 'AngleElbow'; 'AngleShoulder'; ...
             'XLeftShoulder'; 'XRightShoulder'; 'YLeftShoulder'; 'YRightShoulder'; ...
             'VAMC'; 'VAWrist'; 'VAElbow'; 'VAShoulder'; 'PhiScap'; 'VAPhiScap'};
         
for i=1:size(Variables,1)     
str2 = replace(str,'Var', Variables{i});
eval(str2{1});
eval(str2{2});
eval(str2{3});
eval(str2{4});
end
sum = 0;
for i=1:size(Variables,1)
sum = sum + MotionData.GenericCat.DutyFactor.(Variables{i}); 
end
MotionData.GenericCat.DutyFactor.Average = sum/size(Variables,1);







%% Cat's Motion data

%% GRFs
%--------------------------Normalized Fx & Non Normalized Fx (TMot{2,1})-------------------------------------
Sheet = TMot{2, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
L = 0;
R = 0;
for i=1:size(Sheet.Data,2)  
SegmentSide = Sheet.Data.(VariableNames{i}){3};

if SegmentSide == 'LF'
  L = L+1; 
  %--------Normalized
  MotionData.Cases.GRFs.NFx.Left.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));       % N/N
  MotionData.Cases.GRFs.NFx.Left.Matrix(:,L) = MotionData.Cases.GRFs.NFx.Left.(VariableNames{i});               % N/N
  
  %--------Non Normalized
  %--to consider each cat's mass (CM = Case's Mass)
  if contains(VariableNames{i},'blue')
    CM = MotionData.Cases.MLW.Mass.blue;
  elseif contains(VariableNames{i},'inna')
    CM = MotionData.Cases.MLW.Mass.inna;
  elseif contains(VariableNames{i},'karina')
    CM = MotionData.Cases.MLW.Mass.karina;
  elseif contains(VariableNames{i},'maza')
    CM = MotionData.Cases.MLW.Mass.maza;  
  elseif contains(VariableNames{i},'ryazan')
    CM = MotionData.Cases.MLW.Mass.ryazan;   
  elseif contains(VariableNames{i},'sveta')
    CM = MotionData.Cases.MLW.Mass.sveta;
  elseif contains(VariableNames{i},'tula')
    CM = MotionData.Cases.MLW.Mass.tula;    
  end
  MotionData.Cases.GRFs.Fx.Left.(VariableNames{i}) = MotionData.Cases.GRFs.NFx.Left.(VariableNames{i})*g*CM;       % N
  MotionData.Cases.GRFs.Fx.Left.Matrix(:,L) = MotionData.Cases.GRFs.NFx.Left.(VariableNames{i})*g*CM;              % N
  
  
else
  R = R+1; 
  %---Normalized
  MotionData.Cases.GRFs.NFx.Right.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));      % N/N
  MotionData.Cases.GRFs.NFx.Right.Matrix(:,R) = MotionData.Cases.GRFs.NFx.Right.(VariableNames{i});             % N/N
  
  %--------Non Normalized
  %--to consider each cat's mass (CM = Case's Mass)
  if contains(VariableNames{i},'blue')
    CM = MotionData.Cases.MLW.Mass.blue;
  elseif contains(VariableNames{i},'inna')
    CM = MotionData.Cases.MLW.Mass.inna;
  elseif contains(VariableNames{i},'karina')
    CM = MotionData.Cases.MLW.Mass.karina;
  elseif contains(VariableNames{i},'maza')
    CM = MotionData.Cases.MLW.Mass.maza;  
  elseif contains(VariableNames{i},'ryazan')
    CM = MotionData.Cases.MLW.Mass.ryazan;   
  elseif contains(VariableNames{i},'sveta')
    CM = MotionData.Cases.MLW.Mass.sveta;
  elseif contains(VariableNames{i},'tula')
    CM = MotionData.Cases.MLW.Mass.tula;    
  end
  MotionData.Cases.GRFs.Fx.Right.(VariableNames{i}) = MotionData.Cases.GRFs.NFx.Right.(VariableNames{i})*g*CM;       % N
  MotionData.Cases.GRFs.Fx.Right.Matrix(:,R) = MotionData.Cases.GRFs.NFx.Right.(VariableNames{i})*g*CM;              % N
end

end

%---Normalized
MotionData.GenericCat.GRFs.NFx.Right = mean(MotionData.Cases.GRFs.NFx.Right.Matrix, 2);                                                % N/N
MotionData.GenericCat.GRFs.NFx.Left = mean(MotionData.Cases.GRFs.NFx.Left.Matrix, 2);                                                  % N/N
MotionData.GenericCat.GRFs.NFx.Total = mean([MotionData.Cases.GRFs.NFx.Right.Matrix, MotionData.Cases.GRFs.NFx.Left.Matrix], 2);       % N/N

MotionData.GenericCat.GRFs.STDNFx.Right = std(MotionData.Cases.GRFs.NFx.Right.Matrix,[], 2);                                           % N/N
MotionData.GenericCat.GRFs.STDNFx.Left = std(MotionData.Cases.GRFs.NFx.Left.Matrix, [], 2);                                            % N/N
MotionData.GenericCat.GRFs.STDNFx.Total = std([MotionData.Cases.GRFs.NFx.Right.Matrix, MotionData.Cases.GRFs.NFx.Left.Matrix], [], 2); % N/N


%---Non Normalized
GM = MotionData.GenericCat.MLW.Mass;
MotionData.GenericCat.GRFs.Fx.Right = MotionData.GenericCat.GRFs.NFx.Right*g*GM;         % N
MotionData.GenericCat.GRFs.Fx.Left = MotionData.GenericCat.GRFs.NFx.Left*g*GM;           % N
MotionData.GenericCat.GRFs.Fx.Total = MotionData.GenericCat.GRFs.NFx.Total*g*GM;         % N

MotionData.GenericCat.GRFs.STDFx.Right = MotionData.GenericCat.GRFs.STDNFx.Right*g*GM;   % N
MotionData.GenericCat.GRFs.STDFx.Left = MotionData.GenericCat.GRFs.STDNFx.Left*g*GM;     % N
MotionData.GenericCat.GRFs.STDFx.Total = MotionData.GenericCat.GRFs.STDNFx.Total*g*GM;   % N




%--------------------------Normalized Fz & Non Normalized Fz (TMot{3,1})-------------------------------------
Sheet = TMot{3, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
L = 0;
R = 0;
for i=1:size(Sheet.Data,2)  
SegmentSide = Sheet.Data.(VariableNames{i}){3};

if SegmentSide == 'LF'
  L = L+1; 
  %---Normalized
  MotionData.Cases.GRFs.NFz.Left.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));       % N/N
  MotionData.Cases.GRFs.NFz.Left.Matrix(:,L) = MotionData.Cases.GRFs.NFz.Left.(VariableNames{i});               % N/N
  
  %--------Non Normalized
  %--to consider each cat's mass (CM = Case's Mass)
  if contains(VariableNames{i},'blue')
    CM = MotionData.Cases.MLW.Mass.blue;
  elseif contains(VariableNames{i},'inna')
    CM = MotionData.Cases.MLW.Mass.inna;
  elseif contains(VariableNames{i},'karina')
    CM = MotionData.Cases.MLW.Mass.karina;
  elseif contains(VariableNames{i},'maza')
    CM = MotionData.Cases.MLW.Mass.maza;  
  elseif contains(VariableNames{i},'ryazan')
    CM = MotionData.Cases.MLW.Mass.ryazan;   
  elseif contains(VariableNames{i},'sveta')
    CM = MotionData.Cases.MLW.Mass.sveta;
  elseif contains(VariableNames{i},'tula')
    CM = MotionData.Cases.MLW.Mass.tula;    
  end
  MotionData.Cases.GRFs.Fz.Left.(VariableNames{i}) = MotionData.Cases.GRFs.NFz.Left.(VariableNames{i})*g*CM;       % N
  MotionData.Cases.GRFs.Fz.Left.Matrix(:,L) = MotionData.Cases.GRFs.NFz.Left.(VariableNames{i})*g*CM;              % N
  
else
  R = R+1;  
  %---Normalized
  MotionData.Cases.GRFs.NFz.Right.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));      % N/N
  MotionData.Cases.GRFs.NFz.Right.Matrix(:,R) = MotionData.Cases.GRFs.NFz.Right.(VariableNames{i});             % N/N
  
  %--------Non Normalized
  %--to consider each cat's moment (CM = Case's Mass)
  if contains(VariableNames{i},'blue')
    CM = MotionData.Cases.MLW.Mass.blue;
  elseif contains(VariableNames{i},'inna')
    CM = MotionData.Cases.MLW.Mass.inna;
  elseif contains(VariableNames{i},'karina')
    CM = MotionData.Cases.MLW.Mass.karina;
  elseif contains(VariableNames{i},'maza')
    CM = MotionData.Cases.MLW.Mass.maza;  
  elseif contains(VariableNames{i},'ryazan')
    CM = MotionData.Cases.MLW.Mass.ryazan;   
  elseif contains(VariableNames{i},'sveta')
    CM = MotionData.Cases.MLW.Mass.sveta;
  elseif contains(VariableNames{i},'tula')
    CM = MotionData.Cases.MLW.Mass.tula;    
  end
  MotionData.Cases.GRFs.Fz.Right.(VariableNames{i}) = MotionData.Cases.GRFs.NFz.Right.(VariableNames{i})*g*CM;       % N
  MotionData.Cases.GRFs.Fz.Right.Matrix(:,R) = MotionData.Cases.GRFs.NFz.Right.(VariableNames{i})*g*CM;              % N
end

end

%---Normalized
MotionData.GenericCat.GRFs.NFz.Right = mean(MotionData.Cases.GRFs.NFz.Right.Matrix, 2);                                                % N/N
MotionData.GenericCat.GRFs.NFz.Left = mean(MotionData.Cases.GRFs.NFz.Left.Matrix, 2);                                                  % N/N
MotionData.GenericCat.GRFs.NFz.Total = mean([MotionData.Cases.GRFs.NFz.Right.Matrix, MotionData.Cases.GRFs.NFz.Left.Matrix], 2);       % N/N

MotionData.GenericCat.GRFs.STDNFz.Right = std(MotionData.Cases.GRFs.NFz.Right.Matrix,[], 2);                                           % N/N
MotionData.GenericCat.GRFs.STDNFz.Left = std(MotionData.Cases.GRFs.NFz.Left.Matrix, [], 2);                                            % N/N
MotionData.GenericCat.GRFs.STDNFz.Total = std([MotionData.Cases.GRFs.NFz.Right.Matrix, MotionData.Cases.GRFs.NFz.Left.Matrix], [], 2); % N/N


%---Non Normalized
GM = MotionData.GenericCat.MLW.Mass;
MotionData.GenericCat.GRFs.Fz.Right = MotionData.GenericCat.GRFs.NFz.Right*g*GM;         % N
MotionData.GenericCat.GRFs.Fz.Left = MotionData.GenericCat.GRFs.NFz.Left*g*GM;           % N
MotionData.GenericCat.GRFs.Fz.Total = MotionData.GenericCat.GRFs.NFz.Total*g*GM;         % N

MotionData.GenericCat.GRFs.STDFz.Right = MotionData.GenericCat.GRFs.STDNFz.Right*g*GM;   % N
MotionData.GenericCat.GRFs.STDFz.Left = MotionData.GenericCat.GRFs.STDNFz.Left*g*GM;     % N
MotionData.GenericCat.GRFs.STDFz.Total = MotionData.GenericCat.GRFs.STDNFz.Total*g*GM;   % N


%% Joint Moments

%------------------------- Normalized Moment of MC & Non Normalized Moment of MC (TMot{4,1})-------------------------------------
Sheet = TMot{4, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
L = 0;
R = 0;
for i=1:size(Sheet.Data,2)  
SegmentSide = Sheet.Data.(VariableNames{i}){3};

if SegmentSide == 'LF'
  L = L+1; 
  %---Normalized
  MotionData.Cases.Moments.NMomMc.Left.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));       % Nm/Nm
  MotionData.Cases.Moments.NMomMc.Left.Matrix(:,L) = MotionData.Cases.Moments.NMomMc.Left.(VariableNames{i});         % Nm/Nm
  
  %--------Non Normalized
  %--to consider each cat's moment (WinFL = Weight*ForeLimbLength)
  if contains(VariableNames{i},'blue')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.blue; 
  elseif contains(VariableNames{i},'inna')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.inna;
  elseif contains(VariableNames{i},'karina')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.karina;
  elseif contains(VariableNames{i},'maza')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.maza;
  elseif contains(VariableNames{i},'ryazan')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.ryazan;  
  elseif contains(VariableNames{i},'sveta')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.sveta;
  elseif contains(VariableNames{i},'tula')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.tula;    
  end
  MotionData.Cases.Moments.MomMc.Left.(VariableNames{i}) = MotionData.Cases.Moments.NMomMc.Left.(VariableNames{i})*WinFL;    % Nm
  MotionData.Cases.Moments.MomMc.Left.Matrix(:,L) = MotionData.Cases.Moments.NMomMc.Left.(VariableNames{i})*WinFL;           % Nm
  
else
  R = R+1;  
  %---Normalized
  MotionData.Cases.Moments.NMomMc.Right.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));      % Nm/Nm
  MotionData.Cases.Moments.NMomMc.Right.Matrix(:,R) = MotionData.Cases.Moments.NMomMc.Right.(VariableNames{i});       % Nm/Nm
  
    %--------Non Normalized
  %--to consider each cat's moment (WinFL = Weight*ForeLimbLength)
  if contains(VariableNames{i},'blue')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.blue;
  elseif contains(VariableNames{i},'inna')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.inna;
  elseif contains(VariableNames{i},'karina')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.karina;
  elseif contains(VariableNames{i},'maza')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.maza;
  elseif contains(VariableNames{i},'ryazan')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.ryazan;  
  elseif contains(VariableNames{i},'sveta')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.sveta;
  elseif contains(VariableNames{i},'tula')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.tula;    
  end
  MotionData.Cases.Moments.MomMc.Right.(VariableNames{i}) = MotionData.Cases.Moments.NMomMc.Right.(VariableNames{i})*WinFL;    % Nm
  MotionData.Cases.Moments.MomMc.Right.Matrix(:,R) = MotionData.Cases.Moments.NMomMc.Right.(VariableNames{i})*WinFL;           % Nm
  
end

end

%---Normalized
MotionData.GenericCat.Moments.NMomMc.Right = mean(MotionData.Cases.Moments.NMomMc.Right.Matrix, 2);                                                     % Nm/Nm
MotionData.GenericCat.Moments.NMomMc.Left = mean(MotionData.Cases.Moments.NMomMc.Left.Matrix, 2);                                                       % Nm/Nm
MotionData.GenericCat.Moments.NMomMc.Total = mean([MotionData.Cases.Moments.NMomMc.Right.Matrix, MotionData.Cases.Moments.NMomMc.Left.Matrix], 2);       % Nm/Nm

MotionData.GenericCat.Moments.STDNMomMc.Right = std(MotionData.Cases.Moments.NMomMc.Right.Matrix,[], 2);                                                % Nm/Nm
MotionData.GenericCat.Moments.STDNMomMc.Left = std(MotionData.Cases.Moments.NMomMc.Left.Matrix, [], 2);                                                 % Nm/Nm
MotionData.GenericCat.Moments.STDNMomMc.Total = std([MotionData.Cases.Moments.NMomMc.Right.Matrix, MotionData.Cases.Moments.NMomMc.Left.Matrix], [], 2); % Nm/Nm


%---Non Normalized
GWinFL = MotionData.GenericCat.MLW.WeightInForeLimbLength;
MotionData.GenericCat.Moments.MomMc.Right = MotionData.GenericCat.Moments.NMomMc.Right*GWinFL;         % Nm
MotionData.GenericCat.Moments.MomMc.Left = MotionData.GenericCat.Moments.NMomMc.Left*GWinFL;           % Nm
MotionData.GenericCat.Moments.MomMc.Total = MotionData.GenericCat.Moments.NMomMc.Total*GWinFL;         % Nm

MotionData.GenericCat.Moments.STDMomMc.Right = MotionData.GenericCat.Moments.STDNMomMc.Right*GWinFL;   % Nm
MotionData.GenericCat.Moments.STDMomMc.Left = MotionData.GenericCat.Moments.STDNMomMc.Left*GWinFL;     % Nm
MotionData.GenericCat.Moments.STDMomMc.Total = MotionData.GenericCat.Moments.STDNMomMc.Total*GWinFL;   % Nm



%------------------------- Normalized Moment of Wrist & Non Normalized Moment of Wrist (TMot{5,1})-------------------------------------
Sheet = TMot{5, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
L = 0;
R = 0;
for i=1:size(Sheet.Data,2)  
SegmentSide = Sheet.Data.(VariableNames{i}){3};

if SegmentSide == 'LF'
  L = L+1; 
  %---Normalized
  MotionData.Cases.Moments.NMomWrist.Left.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));       % Nm/Nm
  MotionData.Cases.Moments.NMomWrist.Left.Matrix(:,L) = MotionData.Cases.Moments.NMomWrist.Left.(VariableNames{i});      % Nm/Nm
  
  %--------Non Normalized
  %--to consider each cat's moment (WinFL = Weight*ForeLimbLength)
  if contains(VariableNames{i},'blue')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.blue; 
  elseif contains(VariableNames{i},'inna')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.inna;
  elseif contains(VariableNames{i},'karina')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.karina;
  elseif contains(VariableNames{i},'maza')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.maza;
  elseif contains(VariableNames{i},'ryazan')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.ryazan;  
  elseif contains(VariableNames{i},'sveta')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.sveta;
  elseif contains(VariableNames{i},'tula')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.tula;    
  end
  MotionData.Cases.Moments.MomWrist.Left.(VariableNames{i}) = MotionData.Cases.Moments.NMomWrist.Left.(VariableNames{i})*WinFL;    % Nm
  MotionData.Cases.Moments.MomWrist.Left.Matrix(:,L) = MotionData.Cases.Moments.NMomWrist.Left.(VariableNames{i})*WinFL;           % Nm
  
else
  R = R+1;  
  %---Normalized
  MotionData.Cases.Moments.NMomWrist.Right.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));      % Nm/Nm
  MotionData.Cases.Moments.NMomWrist.Right.Matrix(:,R) = MotionData.Cases.Moments.NMomWrist.Right.(VariableNames{i});    % Nm/Nm
  
    %--------Non Normalized
  %--to consider each cat's moment (WinFL = Weight*ForeLimbLength)
  if contains(VariableNames{i},'blue')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.blue;
  elseif contains(VariableNames{i},'inna')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.inna;
  elseif contains(VariableNames{i},'karina')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.karina;
  elseif contains(VariableNames{i},'maza')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.maza;
  elseif contains(VariableNames{i},'ryazan')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.ryazan;  
  elseif contains(VariableNames{i},'sveta')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.sveta;
  elseif contains(VariableNames{i},'tula')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.tula;    
  end
  MotionData.Cases.Moments.MomWrist.Right.(VariableNames{i}) = MotionData.Cases.Moments.NMomWrist.Right.(VariableNames{i})*WinFL;    % Nm
  MotionData.Cases.Moments.MomWrist.Right.Matrix(:,R) = MotionData.Cases.Moments.NMomWrist.Right.(VariableNames{i})*WinFL;           % Nm
  
end

end

%---Normalized
MotionData.GenericCat.Moments.NMomWrist.Right = mean(MotionData.Cases.Moments.NMomWrist.Right.Matrix, 2);                                                     % Nm/Nm
MotionData.GenericCat.Moments.NMomWrist.Left = mean(MotionData.Cases.Moments.NMomWrist.Left.Matrix, 2);                                                       % Nm/Nm
MotionData.GenericCat.Moments.NMomWrist.Total = mean([MotionData.Cases.Moments.NMomWrist.Right.Matrix, MotionData.Cases.Moments.NMomWrist.Left.Matrix], 2);   % Nm/Nm

MotionData.GenericCat.Moments.STDNMomWrist.Right = std(MotionData.Cases.Moments.NMomWrist.Right.Matrix,[], 2);                                                    % Nm/Nm
MotionData.GenericCat.Moments.STDNMomWrist.Left = std(MotionData.Cases.Moments.NMomWrist.Left.Matrix, [], 2);                                                     % Nm/Nm
MotionData.GenericCat.Moments.STDNMomWrist.Total = std([MotionData.Cases.Moments.NMomWrist.Right.Matrix, MotionData.Cases.Moments.NMomWrist.Left.Matrix], [], 2); % Nm/Nm


%---Non Normalized
GWinFL = MotionData.GenericCat.MLW.WeightInForeLimbLength;
MotionData.GenericCat.Moments.MomWrist.Right = MotionData.GenericCat.Moments.NMomWrist.Right*GWinFL;         % Nm
MotionData.GenericCat.Moments.MomWrist.Left = MotionData.GenericCat.Moments.NMomWrist.Left*GWinFL;           % Nm
MotionData.GenericCat.Moments.MomWrist.Total = MotionData.GenericCat.Moments.NMomWrist.Total*GWinFL;         % Nm

MotionData.GenericCat.Moments.STDMomWrist.Right = MotionData.GenericCat.Moments.STDNMomWrist.Right*GWinFL;   % Nm
MotionData.GenericCat.Moments.STDMomWrist.Left = MotionData.GenericCat.Moments.STDNMomWrist.Left*GWinFL;     % Nm
MotionData.GenericCat.Moments.STDMomWrist.Total = MotionData.GenericCat.Moments.STDNMomWrist.Total*GWinFL;   % Nm



%------------------------- Normalized Moment of Elbow & Non Normalized Moment of Elbow (TMot{6,1})-------------------------------------
Sheet = TMot{6, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
L = 0;
R = 0;
for i=1:size(Sheet.Data,2)  
SegmentSide = Sheet.Data.(VariableNames{i}){3};

if SegmentSide == 'LF'
  L = L+1; 
  %---Normalized
  MotionData.Cases.Moments.NMomElbow.Left.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));       % Nm/Nm
  MotionData.Cases.Moments.NMomElbow.Left.Matrix(:,L) = MotionData.Cases.Moments.NMomElbow.Left.(VariableNames{i});      % Nm/Nm
  
  %--------Non Normalized
  %--to consider each cat's moment (WinFL = Weight*ForeLimbLength)
  if contains(VariableNames{i},'blue')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.blue; 
  elseif contains(VariableNames{i},'inna')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.inna;
  elseif contains(VariableNames{i},'karina')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.karina;
  elseif contains(VariableNames{i},'maza')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.maza;
  elseif contains(VariableNames{i},'ryazan')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.ryazan;  
  elseif contains(VariableNames{i},'sveta')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.sveta;
  elseif contains(VariableNames{i},'tula')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.tula;    
  end
  MotionData.Cases.Moments.MomElbow.Left.(VariableNames{i}) = MotionData.Cases.Moments.NMomElbow.Left.(VariableNames{i})*WinFL;    % Nm
  MotionData.Cases.Moments.MomElbow.Left.Matrix(:,L) = MotionData.Cases.Moments.NMomElbow.Left.(VariableNames{i})*WinFL;           % Nm
  
else
  R = R+1;  
  %---Normalized
  MotionData.Cases.Moments.NMomElbow.Right.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));      % Nm/Nm
  MotionData.Cases.Moments.NMomElbow.Right.Matrix(:,R) = MotionData.Cases.Moments.NMomElbow.Right.(VariableNames{i});    % Nm/Nm
  
    %--------Non Normalized
  %--to consider each cat's moment (WinFL = Weight*ForeLimbLength)
  if contains(VariableNames{i},'blue')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.blue;
  elseif contains(VariableNames{i},'inna')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.inna;
  elseif contains(VariableNames{i},'karina')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.karina;
  elseif contains(VariableNames{i},'maza')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.maza;
  elseif contains(VariableNames{i},'ryazan')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.ryazan;  
  elseif contains(VariableNames{i},'sveta')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.sveta;
  elseif contains(VariableNames{i},'tula')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.tula;    
  end
  MotionData.Cases.Moments.MomElbow.Right.(VariableNames{i}) = MotionData.Cases.Moments.NMomElbow.Right.(VariableNames{i})*WinFL;    % Nm
  MotionData.Cases.Moments.MomElbow.Right.Matrix(:,R) = MotionData.Cases.Moments.NMomElbow.Right.(VariableNames{i})*WinFL;           % Nm
  
end

end

%---Normalized
MotionData.GenericCat.Moments.NMomElbow.Right = mean(MotionData.Cases.Moments.NMomElbow.Right.Matrix, 2);                                                     % Nm/Nm
MotionData.GenericCat.Moments.NMomElbow.Left = mean(MotionData.Cases.Moments.NMomElbow.Left.Matrix, 2);                                                       % Nm/Nm
MotionData.GenericCat.Moments.NMomElbow.Total = mean([MotionData.Cases.Moments.NMomElbow.Right.Matrix, MotionData.Cases.Moments.NMomElbow.Left.Matrix], 2);   % Nm/Nm

MotionData.GenericCat.Moments.STDNMomElbow.Right = std(MotionData.Cases.Moments.NMomElbow.Right.Matrix,[], 2);                                                    % Nm/Nm
MotionData.GenericCat.Moments.STDNMomElbow.Left = std(MotionData.Cases.Moments.NMomElbow.Left.Matrix, [], 2);                                                     % Nm/Nm
MotionData.GenericCat.Moments.STDNMomElbow.Total = std([MotionData.Cases.Moments.NMomElbow.Right.Matrix, MotionData.Cases.Moments.NMomElbow.Left.Matrix], [], 2); % Nm/Nm


%---Non Normalized
GWinFL = MotionData.GenericCat.MLW.WeightInForeLimbLength;
MotionData.GenericCat.Moments.MomElbow.Right = MotionData.GenericCat.Moments.NMomElbow.Right*GWinFL;         % Nm
MotionData.GenericCat.Moments.MomElbow.Left = MotionData.GenericCat.Moments.NMomElbow.Left*GWinFL;           % Nm
MotionData.GenericCat.Moments.MomElbow.Total = MotionData.GenericCat.Moments.NMomElbow.Total*GWinFL;         % Nm

MotionData.GenericCat.Moments.STDMomElbow.Right = MotionData.GenericCat.Moments.STDNMomElbow.Right*GWinFL;   % Nm
MotionData.GenericCat.Moments.STDMomElbow.Left = MotionData.GenericCat.Moments.STDNMomElbow.Left*GWinFL;     % Nm
MotionData.GenericCat.Moments.STDMomElbow.Total = MotionData.GenericCat.Moments.STDNMomElbow.Total*GWinFL;   % Nm



%------------------------- Normalized Moment of Shoulder & Non Normalized Moment of Shoulder (TMot{7,1})-------------------------------------
Sheet = TMot{7, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
L = 0;
R = 0;
for i=1:size(Sheet.Data,2)  
SegmentSide = Sheet.Data.(VariableNames{i}){3};

if SegmentSide == 'LF'
  L = L+1; 
  %---Normalized
  MotionData.Cases.Moments.NMomShou.Left.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));       % Nm/Nm
  MotionData.Cases.Moments.NMomShou.Left.Matrix(:,L) = MotionData.Cases.Moments.NMomShou.Left.(VariableNames{i});       % Nm/Nm
  
  %--------Non Normalized
  %--to consider each cat's moment (WinFL = Weight*ForeLimbLength)
  if contains(VariableNames{i},'blue')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.blue;
  elseif contains(VariableNames{i},'inna')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.inna;
  elseif contains(VariableNames{i},'karina')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.karina;
  elseif contains(VariableNames{i},'maza')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.maza;
  elseif contains(VariableNames{i},'ryazan')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.ryazan;  
  elseif contains(VariableNames{i},'sveta')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.sveta;
  elseif contains(VariableNames{i},'tula')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.tula;    
  end
  MotionData.Cases.Moments.MomShou.Left.(VariableNames{i}) = MotionData.Cases.Moments.NMomShou.Left.(VariableNames{i})*WinFL;    % Nm
  MotionData.Cases.Moments.MomShou.Left.Matrix(:,L) = MotionData.Cases.Moments.NMomShou.Left.(VariableNames{i})*WinFL;           % Nm
  
else
  R = R+1;  
  %---Normalized
  MotionData.Cases.Moments.NMomShou.Right.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));      % Nm/Nm
  MotionData.Cases.Moments.NMomShou.Right.Matrix(:,R) = MotionData.Cases.Moments.NMomShou.Right.(VariableNames{i});     % Nm/Nm
  
    %--------Non Normalized
  %--to consider each cat's mass (WinFL = Weight*ForeLimbLength)
  if contains(VariableNames{i},'blue')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.blue;
  elseif contains(VariableNames{i},'inna')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.inna;
  elseif contains(VariableNames{i},'karina')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.karina;
  elseif contains(VariableNames{i},'maza')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.maza;
  elseif contains(VariableNames{i},'ryazan')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.ryazan;  
  elseif contains(VariableNames{i},'sveta')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.sveta;
  elseif contains(VariableNames{i},'tula')
    WinFL = MotionData.Cases.MLW.WeightInForeLimbLength.tula;    
  end
  MotionData.Cases.Moments.MomShou.Right.(VariableNames{i}) = MotionData.Cases.Moments.NMomShou.Right.(VariableNames{i})*WinFL;    % Nm
  MotionData.Cases.Moments.MomShou.Right.Matrix(:,R) = MotionData.Cases.Moments.NMomShou.Right.(VariableNames{i})*WinFL;           % Nm
  
end

end

%---Normalized
MotionData.GenericCat.Moments.NMomShou.Right = mean(MotionData.Cases.Moments.NMomShou.Right.Matrix, 2);                                                     % Nm/Nm
MotionData.GenericCat.Moments.NMomShou.Left = mean(MotionData.Cases.Moments.NMomShou.Left.Matrix, 2);                                                       % Nm/Nm
MotionData.GenericCat.Moments.NMomShou.Total = mean([MotionData.Cases.Moments.NMomShou.Right.Matrix, MotionData.Cases.Moments.NMomShou.Left.Matrix], 2);       % Nm/Nm

MotionData.GenericCat.Moments.STDNMomShou.Right = std(MotionData.Cases.Moments.NMomShou.Right.Matrix,[], 2);                                                % Nm/Nm
MotionData.GenericCat.Moments.STDNMomShou.Left = std(MotionData.Cases.Moments.NMomShou.Left.Matrix, [], 2);                                                 % Nm/Nm
MotionData.GenericCat.Moments.STDNMomShou.Total = std([MotionData.Cases.Moments.NMomShou.Right.Matrix, MotionData.Cases.Moments.NMomShou.Left.Matrix], [], 2); % Nm/Nm


%---Non Normalized
GWinFL = MotionData.GenericCat.MLW.WeightInForeLimbLength;
MotionData.GenericCat.Moments.MomShou.Right = MotionData.GenericCat.Moments.NMomShou.Right*GWinFL;         % Nm
MotionData.GenericCat.Moments.MomShou.Left = MotionData.GenericCat.Moments.NMomShou.Left*GWinFL;           % Nm
MotionData.GenericCat.Moments.MomShou.Total = MotionData.GenericCat.Moments.NMomShou.Total*GWinFL;         % Nm

MotionData.GenericCat.Moments.STDMomShou.Right = MotionData.GenericCat.Moments.STDNMomShou.Right*GWinFL;   % Nm
MotionData.GenericCat.Moments.STDMomShou.Left = MotionData.GenericCat.Moments.STDNMomShou.Left*GWinFL;     % Nm
MotionData.GenericCat.Moments.STDMomShou.Total = MotionData.GenericCat.Moments.STDNMomShou.Total*GWinFL;   % Nm


%% Joint Angles

%------------------------- Mc Angle (TMot{8,1})-------------------------------------
Sheet = TMot{8, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
L = 0;
R = 0;
for i=1:size(Sheet.Data,2)  
SegmentSide = Sheet.Data.(VariableNames{i}){3};

if SegmentSide == 'LF'
  L = L+1;  
  MotionData.Cases.Angles.AngMc.Left.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));    % deg
  MotionData.Cases.Angles.AngMc.Left.Matrix(:,L) = MotionData.Cases.Angles.AngMc.Left.(VariableNames{i});        % deg
else
  R = R+1;  
  MotionData.Cases.Angles.AngMc.Right.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));   % deg
  MotionData.Cases.Angles.AngMc.Right.Matrix(:,R) = MotionData.Cases.Angles.AngMc.Right.(VariableNames{i});      % deg
end

end


MotionData.GenericCat.Angles.AngMc.Right = mean(MotionData.Cases.Angles.AngMc.Right.Matrix, 2);
MotionData.GenericCat.Angles.AngMc.Left = mean(MotionData.Cases.Angles.AngMc.Left.Matrix, 2);
MotionData.GenericCat.Angles.AngMc.Total = mean([MotionData.Cases.Angles.AngMc.Right.Matrix, MotionData.Cases.Angles.AngMc.Left.Matrix], 2);

MotionData.GenericCat.Angles.STDAngMc.Right = std(MotionData.Cases.Angles.AngMc.Right.Matrix,[], 2);
MotionData.GenericCat.Angles.STDAngMc.Left = std(MotionData.Cases.Angles.AngMc.Left.Matrix, [], 2);
MotionData.GenericCat.Angles.STDAngMc.Total = std([MotionData.Cases.Angles.AngMc.Right.Matrix, MotionData.Cases.Angles.AngMc.Left.Matrix], [], 2);




%------------------------- Wrist Angle (TMot{9,1})-------------------------------------
Sheet = TMot{9, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
L = 0;
R = 0;
for i=1:size(Sheet.Data,2)  
SegmentSide = Sheet.Data.(VariableNames{i}){3};

if SegmentSide == 'LF'
  L = L+1;  
  MotionData.Cases.Angles.AngWrist.Left.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));       % deg
  MotionData.Cases.Angles.AngWrist.Left.Matrix(:,L) = MotionData.Cases.Angles.AngWrist.Left.(VariableNames{i});        % deg
else
  R = R+1;  
  MotionData.Cases.Angles.AngWrist.Right.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));      % deg
  MotionData.Cases.Angles.AngWrist.Right.Matrix(:,R) = MotionData.Cases.Angles.AngWrist.Right.(VariableNames{i});      % deg
end

end


MotionData.GenericCat.Angles.AngWrist.Right = mean(MotionData.Cases.Angles.AngWrist.Right.Matrix, 2);
MotionData.GenericCat.Angles.AngWrist.Left = mean(MotionData.Cases.Angles.AngWrist.Left.Matrix, 2);
MotionData.GenericCat.Angles.AngWrist.Total = mean([MotionData.Cases.Angles.AngWrist.Right.Matrix, MotionData.Cases.Angles.AngWrist.Left.Matrix], 2);

MotionData.GenericCat.Angles.STDAngWrist.Right = std(MotionData.Cases.Angles.AngWrist.Right.Matrix,[], 2);
MotionData.GenericCat.Angles.STDAngWrist.Left = std(MotionData.Cases.Angles.AngWrist.Left.Matrix, [], 2);
MotionData.GenericCat.Angles.STDAngWrist.Total = std([MotionData.Cases.Angles.AngWrist.Right.Matrix, MotionData.Cases.Angles.AngWrist.Left.Matrix], [], 2);



%------------------------- Elbow Angle (TMot{10,1})-------------------------------------
Sheet = TMot{10, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
L = 0;
R = 0;
for i=1:size(Sheet.Data,2)  
SegmentSide = Sheet.Data.(VariableNames{i}){3};

if SegmentSide == 'LF'
  L = L+1;  
  MotionData.Cases.Angles.AngElbow.Left.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));    % deg
  MotionData.Cases.Angles.AngElbow.Left.Matrix(:,L) = MotionData.Cases.Angles.AngElbow.Left.(VariableNames{i});     % deg
else
  R = R+1;  
  MotionData.Cases.Angles.AngElbow.Right.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));   % deg
  MotionData.Cases.Angles.AngElbow.Right.Matrix(:,R) = MotionData.Cases.Angles.AngElbow.Right.(VariableNames{i});   % deg
end

end


MotionData.GenericCat.Angles.AngElbow.Right = mean(MotionData.Cases.Angles.AngElbow.Right.Matrix, 2);
MotionData.GenericCat.Angles.AngElbow.Left = mean(MotionData.Cases.Angles.AngElbow.Left.Matrix, 2);
MotionData.GenericCat.Angles.AngElbow.Total = mean([MotionData.Cases.Angles.AngElbow.Right.Matrix, MotionData.Cases.Angles.AngElbow.Left.Matrix], 2);

MotionData.GenericCat.Angles.STDAngElbow.Right = std(MotionData.Cases.Angles.AngElbow.Right.Matrix,[], 2);
MotionData.GenericCat.Angles.STDAngElbow.Left = std(MotionData.Cases.Angles.AngElbow.Left.Matrix, [], 2);
MotionData.GenericCat.Angles.STDAngElbow.Total = std([MotionData.Cases.Angles.AngElbow.Right.Matrix, MotionData.Cases.Angles.AngElbow.Left.Matrix], [], 2);


%------------------------- Shoulder Angle (TMot{11,1})-------------------------------------
Sheet = TMot{11, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
L = 0;
R = 0;
for i=1:size(Sheet.Data,2)  
SegmentSide = Sheet.Data.(VariableNames{i}){3};

if SegmentSide == 'LF'
  L = L+1;  
  MotionData.Cases.Angles.AngShou.Left.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));    % deg
  MotionData.Cases.Angles.AngShou.Left.Matrix(:,L) = MotionData.Cases.Angles.AngShou.Left.(VariableNames{i});      % deg
else
  R = R+1;  
  MotionData.Cases.Angles.AngShou.Right.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));   % deg
  MotionData.Cases.Angles.AngShou.Right.Matrix(:,R) = MotionData.Cases.Angles.AngShou.Right.(VariableNames{i});    % deg
end

end


MotionData.GenericCat.Angles.AngShou.Right = mean(MotionData.Cases.Angles.AngShou.Right.Matrix, 2);
MotionData.GenericCat.Angles.AngShou.Left = mean(MotionData.Cases.Angles.AngShou.Left.Matrix, 2);
MotionData.GenericCat.Angles.AngShou.Total = mean([MotionData.Cases.Angles.AngShou.Right.Matrix, MotionData.Cases.Angles.AngShou.Left.Matrix], 2);

MotionData.GenericCat.Angles.STDAngShou.Right = std(MotionData.Cases.Angles.AngShou.Right.Matrix,[], 2);
MotionData.GenericCat.Angles.STDAngShou.Left = std(MotionData.Cases.Angles.AngShou.Left.Matrix, [], 2);
MotionData.GenericCat.Angles.STDAngShou.Total = std([MotionData.Cases.Angles.AngShou.Right.Matrix, MotionData.Cases.Angles.AngShou.Left.Matrix], [], 2);



%% Joint Angular Velocities

%------------------------- Mc Angular Velocity (TMot{12,1})-------------------------------------
Sheet = TMot{12, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
L = 0;
R = 0;
for i=1:size(Sheet.Data,2)  
SegmentSide = Sheet.Data.(VariableNames{i}){3};

if SegmentSide == 'LF'
  L = L+1;  
  MotionData.Cases.AngularVelocities.VAMc.Left.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));          % deg/s
  MotionData.Cases.AngularVelocities.VAMc.Left.Matrix(:,L) = MotionData.Cases.AngularVelocities.VAMc.Left.(VariableNames{i});    % deg/s
else
  R = R+1;  
  MotionData.Cases.AngularVelocities.VAMc.Right.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));         % deg/s
  MotionData.Cases.AngularVelocities.VAMc.Right.Matrix(:,R) = MotionData.Cases.AngularVelocities.VAMc.Right.(VariableNames{i});  % deg/s
end

end


MotionData.GenericCat.AngularVelocities.VAMc.Right = mean(MotionData.Cases.AngularVelocities.VAMc.Right.Matrix, 2);
MotionData.GenericCat.AngularVelocities.VAMc.Left = mean(MotionData.Cases.AngularVelocities.VAMc.Left.Matrix, 2);
MotionData.GenericCat.AngularVelocities.VAMc.Total = mean([MotionData.Cases.AngularVelocities.VAMc.Right.Matrix, MotionData.Cases.AngularVelocities.VAMc.Left.Matrix], 2);

MotionData.GenericCat.AngularVelocities.STDVAMc.Right = std(MotionData.Cases.AngularVelocities.VAMc.Right.Matrix,[], 2);
MotionData.GenericCat.AngularVelocities.STDVAMc.Left = std(MotionData.Cases.AngularVelocities.VAMc.Left.Matrix, [], 2);
MotionData.GenericCat.AngularVelocities.STDVAMc.Total = std([MotionData.Cases.AngularVelocities.VAMc.Right.Matrix, MotionData.Cases.AngularVelocities.VAMc.Left.Matrix], [], 2);




%------------------------- Wrist Angular Velocity (TMot{13,1})-------------------------------------
Sheet = TMot{13, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
L = 0;
R = 0;
for i=1:size(Sheet.Data,2)  
SegmentSide = Sheet.Data.(VariableNames{i}){3};

if SegmentSide == 'LF'
  L = L+1;  
  MotionData.Cases.AngularVelocities.VAWrist.Left.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));            % deg/s
  MotionData.Cases.AngularVelocities.VAWrist.Left.Matrix(:,L) = MotionData.Cases.AngularVelocities.VAWrist.Left.(VariableNames{i});   % deg/s
else
  R = R+1;  
  MotionData.Cases.AngularVelocities.VAWrist.Right.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));           % deg/s
  MotionData.Cases.AngularVelocities.VAWrist.Right.Matrix(:,R) = MotionData.Cases.AngularVelocities.VAWrist.Right.(VariableNames{i}); % deg/s
end

end


MotionData.GenericCat.AngularVelocities.VAWrist.Right = mean(MotionData.Cases.AngularVelocities.VAWrist.Right.Matrix, 2);
MotionData.GenericCat.AngularVelocities.VAWrist.Left = mean(MotionData.Cases.AngularVelocities.VAWrist.Left.Matrix, 2);
MotionData.GenericCat.AngularVelocities.VAWrist.Total = mean([MotionData.Cases.AngularVelocities.VAWrist.Right.Matrix, MotionData.Cases.AngularVelocities.VAWrist.Left.Matrix], 2);

MotionData.GenericCat.AngularVelocities.STDVAWrist.Right = std(MotionData.Cases.AngularVelocities.VAWrist.Right.Matrix,[], 2);
MotionData.GenericCat.AngularVelocities.STDVAWrist.Left = std(MotionData.Cases.AngularVelocities.VAWrist.Left.Matrix, [], 2);
MotionData.GenericCat.AngularVelocities.STDVAWrist.Total = std([MotionData.Cases.AngularVelocities.VAWrist.Right.Matrix, MotionData.Cases.AngularVelocities.VAWrist.Left.Matrix], [], 2);



%------------------------- Elbow Angular Velocity (TMot{14,1})-------------------------------------
Sheet = TMot{14, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
L = 0;
R = 0;
for i=1:size(Sheet.Data,2)  
SegmentSide = Sheet.Data.(VariableNames{i}){3};

if SegmentSide == 'LF'
  L = L+1;  
  MotionData.Cases.AngularVelocities.VAElbow.Left.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));             % deg/s
  MotionData.Cases.AngularVelocities.VAElbow.Left.Matrix(:,L) = MotionData.Cases.AngularVelocities.VAElbow.Left.(VariableNames{i});    % deg/s
else
  R = R+1;  
  MotionData.Cases.AngularVelocities.VAElbow.Right.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));            % deg/s
  MotionData.Cases.AngularVelocities.VAElbow.Right.Matrix(:,R) = MotionData.Cases.AngularVelocities.VAElbow.Right.(VariableNames{i});  % deg/s
end

end


MotionData.GenericCat.AngularVelocities.VAElbow.Right = mean(MotionData.Cases.AngularVelocities.VAElbow.Right.Matrix, 2);
MotionData.GenericCat.AngularVelocities.VAElbow.Left = mean(MotionData.Cases.AngularVelocities.VAElbow.Left.Matrix, 2);
MotionData.GenericCat.AngularVelocities.VAElbow.Total = mean([MotionData.Cases.AngularVelocities.VAElbow.Right.Matrix, MotionData.Cases.AngularVelocities.VAElbow.Left.Matrix], 2);

MotionData.GenericCat.AngularVelocities.STDVAElbow.Right = std(MotionData.Cases.AngularVelocities.VAElbow.Right.Matrix,[], 2);
MotionData.GenericCat.AngularVelocities.STDVAElbow.Left = std(MotionData.Cases.AngularVelocities.VAElbow.Left.Matrix, [], 2);
MotionData.GenericCat.AngularVelocities.STDVAElbow.Total = std([MotionData.Cases.AngularVelocities.VAElbow.Right.Matrix, MotionData.Cases.AngularVelocities.VAElbow.Left.Matrix], [], 2);


%------------------------- Shoulder Angular Velocity (TMot{15,1})-------------------------------------
Sheet = TMot{15, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
L = 0;
R = 0;
for i=1:size(Sheet.Data,2)  
SegmentSide = Sheet.Data.(VariableNames{i}){3};

if SegmentSide == 'LF'
  L = L+1;  
  MotionData.Cases.AngularVelocities.VAShou.Left.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));            % deg/s
  MotionData.Cases.AngularVelocities.VAShou.Left.Matrix(:,L) = MotionData.Cases.AngularVelocities.VAShou.Left.(VariableNames{i});    % deg/s
else
  R = R+1;  
  MotionData.Cases.AngularVelocities.VAShou.Right.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));           % deg/s
  MotionData.Cases.AngularVelocities.VAShou.Right.Matrix(:,R) = MotionData.Cases.AngularVelocities.VAShou.Right.(VariableNames{i});  % deg/s
end

end


MotionData.GenericCat.AngularVelocities.VAShou.Right = mean(MotionData.Cases.AngularVelocities.VAShou.Right.Matrix, 2);
MotionData.GenericCat.AngularVelocities.VAShou.Left = mean(MotionData.Cases.AngularVelocities.VAShou.Left.Matrix, 2);
MotionData.GenericCat.AngularVelocities.VAShou.Total = mean([MotionData.Cases.AngularVelocities.VAShou.Right.Matrix, MotionData.Cases.AngularVelocities.VAShou.Left.Matrix], 2);

MotionData.GenericCat.AngularVelocities.STDVAShou.Right = std(MotionData.Cases.AngularVelocities.VAShou.Right.Matrix,[], 2);
MotionData.GenericCat.AngularVelocities.STDVAShou.Left = std(MotionData.Cases.AngularVelocities.VAShou.Left.Matrix, [], 2);
MotionData.GenericCat.AngularVelocities.STDVAShou.Total = std([MotionData.Cases.AngularVelocities.VAShou.Right.Matrix, MotionData.Cases.AngularVelocities.VAShou.Left.Matrix], [], 2);



%% Scapula Angle
%------------------------- Scapula Angle (TMot{16,1})-------------------------------------
Sheet = TMot{16, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
L = 0;
R = 0;
for i=1:size(Sheet.Data,2)  
SegmentSide = Sheet.Data.(VariableNames{i}){3};

if SegmentSide == 'LF'
  L = L+1;  
  MotionData.Cases.Angles.AngScap.Left.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));    % deg
  MotionData.Cases.Angles.AngScap.Left.Matrix(:,L) = MotionData.Cases.Angles.AngScap.Left.(VariableNames{i});      % deg
else
  R = R+1;  
  MotionData.Cases.Angles.AngScap.Right.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));   % deg
  MotionData.Cases.Angles.AngScap.Right.Matrix(:,R) = MotionData.Cases.Angles.AngScap.Right.(VariableNames{i});    % deg
end

end


MotionData.GenericCat.Angles.AngScap.Right = mean(MotionData.Cases.Angles.AngScap.Right.Matrix, 2);
MotionData.GenericCat.Angles.AngScap.Left = mean(MotionData.Cases.Angles.AngScap.Left.Matrix, 2);
MotionData.GenericCat.Angles.AngScap.Total = mean([MotionData.Cases.Angles.AngScap.Right.Matrix, MotionData.Cases.Angles.AngScap.Left.Matrix], 2);

MotionData.GenericCat.Angles.STDAngScap.Right = std(MotionData.Cases.Angles.AngScap.Right.Matrix,[], 2);
MotionData.GenericCat.Angles.STDAngScap.Left = std(MotionData.Cases.Angles.AngScap.Left.Matrix, [], 2);
MotionData.GenericCat.Angles.STDAngScap.Total = std([MotionData.Cases.Angles.AngScap.Right.Matrix, MotionData.Cases.Angles.AngScap.Left.Matrix], [], 2);



%% Scapula Angular Velocity
%------------------------- Scapula Angular Velocity (TMot{17,1})-------------------------------------
Sheet = TMot{17, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
L = 0;
R = 0;
for i=1:size(Sheet.Data,2)  
SegmentSide = Sheet.Data.(VariableNames{i}){3};

if SegmentSide == 'LF'
  L = L+1;  
  MotionData.Cases.AngularVelocities.VAScap.Left.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));            % deg/s
  MotionData.Cases.AngularVelocities.VAScap.Left.Matrix(:,L) = MotionData.Cases.AngularVelocities.VAScap.Left.(VariableNames{i});    % deg/s
else
  R = R+1;  
  MotionData.Cases.AngularVelocities.VAScap.Right.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));           % deg/s
  MotionData.Cases.AngularVelocities.VAScap.Right.Matrix(:,R) = MotionData.Cases.AngularVelocities.VAScap.Right.(VariableNames{i});  % deg/s
end

end


MotionData.GenericCat.AngularVelocities.VAScap.Right = mean(MotionData.Cases.AngularVelocities.VAScap.Right.Matrix, 2);
MotionData.GenericCat.AngularVelocities.VAScap.Left = mean(MotionData.Cases.AngularVelocities.VAScap.Left.Matrix, 2);
MotionData.GenericCat.AngularVelocities.VAScap.Total = mean([MotionData.Cases.AngularVelocities.VAScap.Right.Matrix, MotionData.Cases.AngularVelocities.VAScap.Left.Matrix], 2);

MotionData.GenericCat.AngularVelocities.STDVAScap.Right = std(MotionData.Cases.AngularVelocities.VAScap.Right.Matrix,[], 2);
MotionData.GenericCat.AngularVelocities.STDVAScap.Left = std(MotionData.Cases.AngularVelocities.VAScap.Left.Matrix, [], 2);
MotionData.GenericCat.AngularVelocities.STDVAScap.Total = std([MotionData.Cases.AngularVelocities.VAScap.Right.Matrix, MotionData.Cases.AngularVelocities.VAScap.Left.Matrix], [], 2);



%% Shoulder Coordinates

%------------------------- Normalized X-Coordinate of Shoulder & Non Normalized X-Coordinate of Shoulder (TMot{18,1})-------------------------------------
Sheet = TMot{18, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
L = 0;
R = 0;
for i=1:size(Sheet.Data,2)  
SegmentSide = Sheet.Data.(VariableNames{i}){3};

if SegmentSide == 'LF'
  L = L+1; 
  %---Non Normalized
  MotionData.Cases.Coordinates.xSho.Left.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));       % m
  MotionData.Cases.Coordinates.xSho.Left.Matrix(:,L) = MotionData.Cases.Coordinates.xSho.Left.(VariableNames{i});       % m
  
  %--------Normalized
  %--to consider each cat's fore limb length (FL = Weight*ForeLimbLength)
  if contains(VariableNames{i},'blue')
    FL = MotionData.Cases.MLW.ForeLimbLength.blue;
  elseif contains(VariableNames{i},'inna')
    FL = MotionData.Cases.MLW.ForeLimbLength.inna;
  elseif contains(VariableNames{i},'karina')
    FL = MotionData.Cases.MLW.ForeLimbLength.karina;
  elseif contains(VariableNames{i},'maza')
    FL = MotionData.Cases.MLW.ForeLimbLength.maza;
  elseif contains(VariableNames{i},'ryazan')
    FL = MotionData.Cases.MLW.ForeLimbLength.ryazan;  
  elseif contains(VariableNames{i},'sveta')
    FL = MotionData.Cases.MLW.ForeLimbLength.sveta;
  elseif contains(VariableNames{i},'tula')
    FL = MotionData.Cases.MLW.ForeLimbLength.tula;    
  end
  MotionData.Cases.Coordinates.NxSho.Left.(VariableNames{i}) = MotionData.Cases.Coordinates.xSho.Left.(VariableNames{i})/FL;    % m/m
  MotionData.Cases.Coordinates.NxSho.Left.Matrix(:,L) = MotionData.Cases.Coordinates.xSho.Left.(VariableNames{i})/FL;           % m/m
  
else
  R = R+1;  
  %---Non Normalized
  MotionData.Cases.Coordinates.xSho.Right.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));      % m
  MotionData.Cases.Coordinates.xSho.Right.Matrix(:,R) = MotionData.Cases.Coordinates.xSho.Right.(VariableNames{i});     % m
  
    %--------Normalized
  %--to consider each cat's fore limb length (FL = Weight*ForeLimbLength)
  if contains(VariableNames{i},'blue')
    FL = MotionData.Cases.MLW.ForeLimbLength.blue;
  elseif contains(VariableNames{i},'inna')
    FL = MotionData.Cases.MLW.ForeLimbLength.inna;
  elseif contains(VariableNames{i},'karina')
    FL = MotionData.Cases.MLW.ForeLimbLength.karina;
  elseif contains(VariableNames{i},'maza')
    FL = MotionData.Cases.MLW.ForeLimbLength.maza;
  elseif contains(VariableNames{i},'ryazan')
    FL = MotionData.Cases.MLW.ForeLimbLength.ryazan;  
  elseif contains(VariableNames{i},'sveta')
    FL = MotionData.Cases.MLW.ForeLimbLength.sveta;
  elseif contains(VariableNames{i},'tula')
    FL = MotionData.Cases.MLW.ForeLimbLength.tula;    
  end
  MotionData.Cases.Coordinates.NxSho.Right.(VariableNames{i}) = MotionData.Cases.Coordinates.xSho.Right.(VariableNames{i})/FL;    % m/m
  MotionData.Cases.Coordinates.NxSho.Right.Matrix(:,R) = MotionData.Cases.Coordinates.xSho.Right.(VariableNames{i})/FL;           % m/m
  
end

end

%---Normalized
MotionData.GenericCat.Coordinates.NxSho.Right = mean(MotionData.Cases.Coordinates.NxSho.Right.Matrix, 2);                                                     % m/m
MotionData.GenericCat.Coordinates.NxSho.Left = mean(MotionData.Cases.Coordinates.NxSho.Left.Matrix, 2);                                                       % m/m
MotionData.GenericCat.Coordinates.NxSho.Total = mean([MotionData.Cases.Coordinates.NxSho.Right.Matrix, MotionData.Cases.Coordinates.NxSho.Left.Matrix], 2);   % m/m

MotionData.GenericCat.Coordinates.STDNxSho.Right = std(MotionData.Cases.Coordinates.NxSho.Right.Matrix,[], 2);                                                    % m/m
MotionData.GenericCat.Coordinates.STDNxSho.Left = std(MotionData.Cases.Coordinates.NxSho.Left.Matrix, [], 2);                                                     % m/m
MotionData.GenericCat.Coordinates.STDNxSho.Total = std([MotionData.Cases.Coordinates.NxSho.Right.Matrix, MotionData.Cases.Coordinates.NxSho.Left.Matrix], [], 2); % m/m


%---Non Normalized
GFL = MotionData.GenericCat.MLW.ForeLimbLength;
MotionData.GenericCat.Coordinates.xSho.Right = MotionData.GenericCat.Coordinates.NxSho.Right*GFL;         % m
MotionData.GenericCat.Coordinates.xSho.Left = MotionData.GenericCat.Coordinates.NxSho.Left*GFL;           % m
MotionData.GenericCat.Coordinates.xSho.Total = MotionData.GenericCat.Coordinates.NxSho.Total*GFL;         % m

MotionData.GenericCat.Coordinates.STDxSho.Right = MotionData.GenericCat.Coordinates.STDNxSho.Right*GFL;   % m
MotionData.GenericCat.Coordinates.STDxSho.Left = MotionData.GenericCat.Coordinates.STDNxSho.Left*GFL;     % m
MotionData.GenericCat.Coordinates.STDxSho.Total = MotionData.GenericCat.Coordinates.STDNxSho.Total*GFL;   % m


%------------------------- Normalized Z-Coordinate of Shoulder & Non Normalized Z-Coordinate of Shoulder (TMot{19,1})-------------------------------------
Sheet = TMot{19, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
L = 0;
R = 0;
for i=1:size(Sheet.Data,2)  
SegmentSide = Sheet.Data.(VariableNames{i}){3};

if SegmentSide == 'LF'
  L = L+1; 
  %---Non Normalized
  MotionData.Cases.Coordinates.ySho.Left.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));       % m
  MotionData.Cases.Coordinates.ySho.Left.Matrix(:,L) = MotionData.Cases.Coordinates.ySho.Left.(VariableNames{i});       % m
  
  %--------Normalized
  %--to consider each cat's fore limb length (FL = Weight*ForeLimbLength)
  if contains(VariableNames{i},'blue')
    FL = MotionData.Cases.MLW.ForeLimbLength.blue;
  elseif contains(VariableNames{i},'inna')
    FL = MotionData.Cases.MLW.ForeLimbLength.inna;
  elseif contains(VariableNames{i},'karina')
    FL = MotionData.Cases.MLW.ForeLimbLength.karina;
  elseif contains(VariableNames{i},'maza')
    FL = MotionData.Cases.MLW.ForeLimbLength.maza;
  elseif contains(VariableNames{i},'ryazan')
    FL = MotionData.Cases.MLW.ForeLimbLength.ryazan;  
  elseif contains(VariableNames{i},'sveta')
    FL = MotionData.Cases.MLW.ForeLimbLength.sveta;
  elseif contains(VariableNames{i},'tula')
    FL = MotionData.Cases.MLW.ForeLimbLength.tula;    
  end
  MotionData.Cases.Coordinates.NySho.Left.(VariableNames{i}) = MotionData.Cases.Coordinates.ySho.Left.(VariableNames{i})/FL;    % m/m
  MotionData.Cases.Coordinates.NySho.Left.Matrix(:,L) = MotionData.Cases.Coordinates.ySho.Left.(VariableNames{i})/FL;           % m/m
  
else
  R = R+1;  
  %---Non Normalized
  MotionData.Cases.Coordinates.ySho.Right.(VariableNames{i}) = str2double(Sheet.Data.(VariableNames{i})(4:end,1));      % m
  MotionData.Cases.Coordinates.ySho.Right.Matrix(:,R) = MotionData.Cases.Coordinates.ySho.Right.(VariableNames{i});     % m
  
    %--------Normalized
  %--to consider each cat's fore limb length (FL = Weight*ForeLimbLength)
  if contains(VariableNames{i},'blue')
    FL = MotionData.Cases.MLW.ForeLimbLength.blue;
  elseif contains(VariableNames{i},'inna')
    FL = MotionData.Cases.MLW.ForeLimbLength.inna;
  elseif contains(VariableNames{i},'karina')
    FL = MotionData.Cases.MLW.ForeLimbLength.karina;
  elseif contains(VariableNames{i},'maza')
    FL = MotionData.Cases.MLW.ForeLimbLength.maza;
  elseif contains(VariableNames{i},'ryazan')
    FL = MotionData.Cases.MLW.ForeLimbLength.ryazan;  
  elseif contains(VariableNames{i},'sveta')
    FL = MotionData.Cases.MLW.ForeLimbLength.sveta;
  elseif contains(VariableNames{i},'tula')
    FL = MotionData.Cases.MLW.ForeLimbLength.tula;    
  end
  MotionData.Cases.Coordinates.NySho.Right.(VariableNames{i}) = MotionData.Cases.Coordinates.ySho.Right.(VariableNames{i})/FL;    % m/m
  MotionData.Cases.Coordinates.NySho.Right.Matrix(:,R) = MotionData.Cases.Coordinates.ySho.Right.(VariableNames{i})/FL;           % m/m
  
end

end

%---Normalized
MotionData.GenericCat.Coordinates.NySho.Right = mean(MotionData.Cases.Coordinates.NySho.Right.Matrix, 2);                                                     % m/m
MotionData.GenericCat.Coordinates.NySho.Left = mean(MotionData.Cases.Coordinates.NySho.Left.Matrix, 2);                                                       % m/m
MotionData.GenericCat.Coordinates.NySho.Total = mean([MotionData.Cases.Coordinates.NySho.Right.Matrix, MotionData.Cases.Coordinates.NySho.Left.Matrix], 2);   % m/m

MotionData.GenericCat.Coordinates.STDNySho.Right = std(MotionData.Cases.Coordinates.NySho.Right.Matrix,[], 2);                                                    % m/m
MotionData.GenericCat.Coordinates.STDNySho.Left = std(MotionData.Cases.Coordinates.NySho.Left.Matrix, [], 2);                                                     % m/m
MotionData.GenericCat.Coordinates.STDNySho.Total = std([MotionData.Cases.Coordinates.NySho.Right.Matrix, MotionData.Cases.Coordinates.NySho.Left.Matrix], [], 2); % m/m


%---Non Normalized
GFL = MotionData.GenericCat.MLW.ForeLimbLength;
MotionData.GenericCat.Coordinates.ySho.Right = MotionData.GenericCat.Coordinates.NySho.Right*GFL;         % m
MotionData.GenericCat.Coordinates.ySho.Left = MotionData.GenericCat.Coordinates.NySho.Left*GFL;           % m
MotionData.GenericCat.Coordinates.ySho.Total = MotionData.GenericCat.Coordinates.NySho.Total*GFL;         % m

MotionData.GenericCat.Coordinates.STDySho.Right = MotionData.GenericCat.Coordinates.STDNySho.Right*GFL;   % m
MotionData.GenericCat.Coordinates.STDySho.Left = MotionData.GenericCat.Coordinates.STDNySho.Left*GFL;     % m
MotionData.GenericCat.Coordinates.STDySho.Total = MotionData.GenericCat.Coordinates.STDNySho.Total*GFL;   % m






%% Forelimb length
%------------------------- Forelimb length-----------------------------------------------------------------------------
Sheet = TMot{24, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
L = 0;
R = 0;
for i=1:size(Sheet.Data,2)  
SegmentSide = Sheet.Data.(VariableNames{i}){3};

if SegmentSide == 'LF'
  L = L+1;  
  MotionData.Cases.ForelimbLength.Left.(VariableNames{i}) = cell2mat(Sheet.Data.(VariableNames{i})(4:end,1));   % m
  MotionData.Cases.ForelimbLength.Left.Matrix(:,L) = MotionData.Cases.ForelimbLength.Left.(VariableNames{i});   % m
else
  R = R+1;  
  MotionData.Cases.ForelimbLength.Right.(VariableNames{i}) = cell2mat(Sheet.Data.(VariableNames{i})(4:end,1));  % m
  MotionData.Cases.ForelimbLength.Right.Matrix(:,R) = MotionData.Cases.ForelimbLength.Right.(VariableNames{i}); % m
end

end


MotionData.GenericCat.ForelimbLength.Right = mean(MotionData.Cases.ForelimbLength.Right.Matrix, 2);
MotionData.GenericCat.ForelimbLength.Left = mean(MotionData.Cases.ForelimbLength.Left.Matrix, 2);
MotionData.GenericCat.ForelimbLength.Total = mean([MotionData.Cases.ForelimbLength.Right.Matrix, MotionData.Cases.ForelimbLength.Left.Matrix], 2);




%% Forelimb orientation
%------------------------- Forelimb orientation-----------------------------------------------------------------------------
Sheet = TMot{25, 1};
VariableNames = Sheet.Data.Properties.VariableNames;
L = 0;
R = 0;
for i=1:size(Sheet.Data,2)  
SegmentSide = Sheet.Data.(VariableNames{i}){3};

if SegmentSide == 'LF'
  L = L+1;  
  MotionData.Cases.ForelimbOrientation.Left.(VariableNames{i}) = cell2mat(Sheet.Data.(VariableNames{i})(4:end,1));   % m
  MotionData.Cases.ForelimbOrientation.Left.Matrix(:,L) = MotionData.Cases.ForelimbOrientation.Left.(VariableNames{i});   % m
else
  R = R+1;  
  MotionData.Cases.ForelimbOrientation.Right.(VariableNames{i}) = cell2mat(Sheet.Data.(VariableNames{i})(4:end,1));  % m
  MotionData.Cases.ForelimbOrientation.Right.Matrix(:,R) = MotionData.Cases.ForelimbOrientation.Right.(VariableNames{i}); % m
end

end


MotionData.GenericCat.ForelimbOrientation.Right = mean(MotionData.Cases.ForelimbOrientation.Right.Matrix, 2);
MotionData.GenericCat.ForelimbOrientation.Left = mean(MotionData.Cases.ForelimbOrientation.Left.Matrix, 2);
MotionData.GenericCat.ForelimbOrientation.Total = mean([MotionData.Cases.ForelimbOrientation.Right.Matrix, MotionData.Cases.ForelimbOrientation.Left.Matrix], 2);






%%
save('MotionData.mat', 'MotionData');





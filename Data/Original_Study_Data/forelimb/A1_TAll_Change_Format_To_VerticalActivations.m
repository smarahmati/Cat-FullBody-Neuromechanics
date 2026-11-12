clear
clc

load('TAll.mat');

MuscleNames = {'BB';'ECR';'FCU';'PT';'SPS';'TLONG';'TLAT';'BR';'TJ';'ECU';'SD'};
EMG_NormAll{size(MuscleNames,1),1} = {};

varNames = MuscleNames;

% Reformating
for MN=1:size(TAll,1)
  for j=1:length(TAll{MN, 1}.Data.EMG)
      EMG_NormVec = TAll{MN, 1}.Data.EMG{j,1};

      if isa(EMG_NormAll{MN,1},'cell') == 1
        EMG_NormAll{MN,1} = [cell2mat(EMG_NormAll{MN,1}), EMG_NormVec];
      else
        EMG_NormAll{MN,1} = [EMG_NormAll{MN,1}, EMG_NormVec];
      end

  end
end

% Adding DF
for MN=1:size(TAll,1)
 EMG_NormAll{MN,1} = [EMG_NormAll{MN,1}; nan*ones(1,length(TAll{MN, 1}.Data.EMG)); (1-TAll{MN, 1}.Data.DF)'*100];
end




for MN = 1:size(MuscleNames,1)
T = table(EMG_NormAll{MN,1},'VariableNames',{varNames{MN,1}});
filename = 'ForeLimbMuscles_EMG_Vertical.xlsx';
writetable(T,filename,'Sheet',MuscleNames{MN,1});
end




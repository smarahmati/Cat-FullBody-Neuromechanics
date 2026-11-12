clear
clc

load('Activations.mat');
load('Activations_9Groups.mat');
load('MotionData.mat');
load('MuscleLengthVelocityMomentArm.mat');
load('Activations.mat');
load('MuscleMPScaled.mat');
load('MuscleForceMoment.mat');
load('OptimizedMuscleForceMoment.mat');

MuscleNames_9Groups = {'BB';'ECR';'FCU';'PT';'SPS';'TLONG';'TLAT';'BR';'TJ';'ECU';'SD'}; %From EMGs
MuscleNames_9Groups = {'Act:BB, EMGs:BB','Act:Elbow & Wrist flexors, EMGs:ECR', 'Act:Wrist extensors, EMGs:FCU', 'Act:Elbow flexors, EMGs:PT & BR', ...
                       'Act:Shoulder protractors, EMGs:SPS', 'Act:TLONG, EMGs:TLONG', 'Act:Elbow extensors, EMGs:TLAT','Act:Elbow flexors, EMGs:PT & BR', ...
                       'Act:Shoulder retractors, EMGs: TJ & SD', 'EMGs:ECU', 'Act:Shoulder retractors, EMGs:TJ & SD'}; % From 9 Groups


for i=1:length(Activations)
MuscleNames_Acts{i,1} = Activations{i, 1}.Name;
end

for i=1:length(Activations_9Groups)
MuscleNames_Acts_9Groups{i,1} = Activations_9Groups{i, 1}.Name;
end


% load('Cluster_Function.mat');
Color_9 = [[0 1 0]; [0 0 1]; [0 1 1]; ...
        [0.4940 0.1840 0.5560]; [0.4660 0.6740 0.1880]; ...
        [0.3010 0.7450 0.9330]; [0.6350 0.0780 0.1840]; [1 0 1]; [0.75, 0.75, 0]];

% time
CT = MotionData.GenericCat.CycleTime.Average;
dt = CT/(size(MuscleLengthVelocityMomentArm{1, 1}.Length,1)-1);
time = (0:size(MuscleLengthVelocityMomentArm{1, 1}.Length,1)-1)'*dt;
Ntime = time/max(time);
Ndt = Ntime(2)-Ntime(1);


[~,sheet_name]=xlsfinfo('ForeLimbMuscles_EMG_Vertical.xlsx');
for k=1:numel(sheet_name)
  data{k} = xlsread('ForeLimbMuscles_EMG_Vertical.xlsx',sheet_name{k});
end
data = data';




DF_ReSt = round(MotionData.GenericCat.DutyFactor.Average,2); 
DF_ReSw = 1-DF_ReSt;

E_S = 101;  % end of step
DF_S = 103; % duty factor step


for i=1:size(data,1)

for j=1:size(data{i,1},2)
    
DF_Sw = round(data{i,1}(DF_S,j)/100,2);
DF_St = 1-DF_Sw;

Ndt_Sw = Ndt*(DF_ReSw/DF_Sw);
Ndt_St = Ndt*(DF_ReSt/DF_St);
Ntime_Sw = (0:Ndt_Sw:DF_ReSw)';
Ntime_St = (DF_ReSw:Ndt_St:1)';
Ntime_adj{i,1}(:,j) = [Ntime_Sw; Ntime_St(2:end,1)];


% spline fit 
p = 0.999999999999;
options = fitoptions('Method','Smooth','SmoothingParam',p);
fitobject = fit(Ntime_adj{i,1}(:,j), data{i,1}(1:E_S,j),'smoothingspline',options);
EMG_adj{i,1}(:,j) = fitobject (Ntime);
end

end



% Mean values
for i=1:size(EMG_adj,1)
 EMG_adj_mean{i,1} = mean(EMG_adj{i,1}, 2);
end

% Similar muscles to the MuscleNames_9Groups from MuscleNames_Acts & MuscleNames_Acts_9Groups
Idx_EMGs = (1:length(MuscleNames_9Groups))';
Idx_Acts = [3; 7; 16; 32; 34; 38; 37; 5; 36; nan; 33];
Idx_Acts_9Groups = [3; 5; 7; 4; 1; 9; 2; 4; 8; nan; 8];


% Computation of Ku
for i=1:length(Idx_EMGs)
  if isnan(Idx_Acts_9Groups(i)) == 0
      Ku(Idx_Acts_9Groups(i),1) = max(Activations_9Groups{Idx_Acts_9Groups(i)}.a)/max(EMG_adj_mean{Idx_EMGs(i), 1});
      % if Ku(Idx_Acts_9Groups(i),1)>=1
      %     Activations_9Groups{Idx_Acts_9Groups(i)}.a = (1/Ku(Idx_Acts_9Groups(i),1))*Activations_9Groups{Idx_Acts_9Groups(i)}.a;
      %     Ku(Idx_Acts_9Groups(i),1)=1;
      % end
  end
end

% Adjusting EMG_adj_mean based on Ku
for i=1:length(Idx_EMGs)
  if isnan(Idx_Acts_9Groups(i)) == 0
     EMG_adj_mean{Idx_EMGs(i), 1} = Ku(Idx_Acts_9Groups(i),1)*EMG_adj_mean{Idx_EMGs(i), 1};
  end
end


% Adjusting EMG_adj based on Ku
for i=1:length(Idx_EMGs)
   if isnan(Idx_Acts_9Groups(i)) == 0
     EMG_adj{Idx_EMGs(i), 1} = Ku(Idx_Acts_9Groups(i),1)*EMG_adj{Idx_EMGs(i), 1};
   end
end






%% plot
figure(1)
% nexttile

grayColor = [.7 .7 .71];

subplot(3,3,1)
MN = 1; % based on EMGs
y1 = EMG_adj_mean{Idx_EMGs(MN), 1};
y2 = Activations{Idx_Acts(MN)}.a;
y3 = Activations_9Groups{Idx_Acts_9Groups(MN)}.a;
y4 = EMG_adj{Idx_EMGs(MN), 1};

STD = std(y4')';
y1_up = y1+STD;
y1_down = y1-STD;
pp = patch([Ntime*100; Ntime(end:-1:1)*100], [y1_down; y1_up(end:-1:1)], grayColor, 'EdgeColor', 'none');
hold on

p1 = plot(Ntime*100, y1,'k','LineWidth',1.5);
hold on
p2 = plot(Ntime*100, y3,'LineWidth',1.5, 'Color', Color_9(Idx_Acts_9Groups(MN),:));
hold on

xl = xline((1-MotionData.GenericCat.DutyFactor.Average)*100,':');
xl.LineWidth = 2;
legend([p1 pp p2], 'Mean EMG', 'STD EMGs','Act from 9');
title(MuscleNames_9Groups(MN))
% xlabel('Normalized cycle time, %')
ylabel('Act')
% set(gca,'XTick',[])
ytickformat('%.2f')
ylim([0 max([max(y3) max(y1_up)])])
box on
R4 = corrcoef(EMG_adj_mean{Idx_EMGs(MN), 1}, Activations{Idx_Acts(MN)}.a)


subplot(3,3,2)
MN = 2; % based on EMGs
y1 = EMG_adj_mean{Idx_EMGs(MN), 1};
y2 = Activations{Idx_Acts(MN)}.a;
y3 = Activations_9Groups{Idx_Acts_9Groups(MN)}.a;
y4 = EMG_adj{Idx_EMGs(MN), 1};

STD = std(y4')';
y1_up = y1+STD;
y1_down = y1-STD;
pp = patch([Ntime*100; Ntime(end:-1:1)*100], [y1_down ;y1_up(end:-1:1)], grayColor, 'EdgeColor', 'none');
hold on

p1 = plot(Ntime*100, y1,'k','LineWidth',1.5);
hold on
p2 = plot(Ntime*100, y3,'LineWidth',1.5, 'Color', Color_9(Idx_Acts_9Groups(MN),:));
hold on

xl = xline((1-MotionData.GenericCat.DutyFactor.Average)*100,':');
xl.LineWidth = 2;
legend([p1 pp p2], 'Mean EMG', 'STD EMGs','Act from 9');
title(MuscleNames_9Groups(MN))
% xlabel('Normalized cycle time, %')
ylabel('Act')
% set(gca,'XTick',[])
ytickformat('%.2f')
ylim([0 max([max(y3) max(y1_up)])])
box on
R4 = corrcoef(EMG_adj_mean{Idx_EMGs(MN), 1}, Activations{Idx_Acts(MN)}.a)


subplot(3,3,3)
MN = 3; % based on EMGs
y1 = EMG_adj_mean{Idx_EMGs(MN), 1};
y2 = Activations{Idx_Acts(MN)}.a;
y3 = Activations_9Groups{Idx_Acts_9Groups(MN)}.a;
y4 = EMG_adj{Idx_EMGs(MN), 1};

STD = std(y4')';
y1_up = y1+STD;
y1_down = y1-STD;
pp = patch([Ntime*100; Ntime(end:-1:1)*100], [y1_down ;y1_up(end:-1:1)], grayColor, 'EdgeColor', 'none');
hold on

p1 = plot(Ntime*100, y1,'k','LineWidth',1.5);
hold on
p2 = plot(Ntime*100, y3,'LineWidth',1.5, 'Color', Color_9(Idx_Acts_9Groups(MN),:));
hold on

xl = xline((1-MotionData.GenericCat.DutyFactor.Average)*100,':');
xl.LineWidth = 2;
legend([p1 pp p2], 'Mean EMG', 'STD EMGs','Act from 9');
title(MuscleNames_9Groups(MN))
% xlabel('Normalized cycle time, %')
ylabel('Act')
% set(gca,'XTick',[])
ytickformat('%.2f')
ylim([0 max([max(y3) max(y1_up)])])
box on
R4 = corrcoef(EMG_adj_mean{Idx_EMGs(MN), 1}, Activations{Idx_Acts(MN)}.a)



subplot(3,3,4)
MN = 4; % based on EMGs (PT) -> Elbow flexor
y1_1 = EMG_adj_mean{Idx_EMGs(MN), 1};
y2_1 = Activations{Idx_Acts(MN)}.a;
y3_1 = Activations_9Groups{Idx_Acts_9Groups(MN)}.a;
y4_1 = EMG_adj{Idx_EMGs(MN), 1};

MN = 8; % based on EMGs (Br) -> Elbow flexor
y1_2 = EMG_adj_mean{Idx_EMGs(MN), 1};
y2_2 = Activations{Idx_Acts(MN)}.a;
y3_2 = Activations_9Groups{Idx_Acts_9Groups(MN)}.a;
y4_2 = EMG_adj{Idx_EMGs(MN), 1};

y1 = mean([y1_1,y1_2], 2);
if y3_1==y3_2; y3= y3_1; end
y4 = [y4_1, y4_2];
hold on;

STD = std(y4')';
y1_up = y1+STD;
y1_down = y1-STD;
pp = patch([Ntime*100; Ntime(end:-1:1)*100], [y1_down ;y1_up(end:-1:1)], grayColor, 'EdgeColor', 'none');
hold on

p1 = plot(Ntime*100, y1,'k','LineWidth',1.5);
hold on
p2 = plot(Ntime*100, y3,'LineWidth',1.5, 'Color', Color_9(Idx_Acts_9Groups(MN),:));
hold on

xl = xline((1-MotionData.GenericCat.DutyFactor.Average)*100,':');
xl.LineWidth = 2;
legend([p1 pp p2], 'Mean EMG', 'STD EMGs','Act from 9');
title(MuscleNames_9Groups(MN))
% xlabel('Normalized cycle time, %')
ylabel('Act')
% set(gca,'XTick',[])
ytickformat('%.2f')
ylim([0 max([max(y3) max(y1_up)])])
box on
R4 = corrcoef(EMG_adj_mean{Idx_EMGs(MN), 1}, Activations{Idx_Acts(MN)}.a)



subplot(3,3,5)
MN = 5; % based on EMGs
y1 = EMG_adj_mean{Idx_EMGs(MN), 1};
y2 = Activations{Idx_Acts(MN)}.a;
y3 = Activations_9Groups{Idx_Acts_9Groups(MN)}.a;
y4 = EMG_adj{Idx_EMGs(MN), 1};

STD = std(y4')';
y1_up = y1+STD;
y1_down = y1-STD;
pp = patch([Ntime*100; Ntime(end:-1:1)*100], [y1_down ;y1_up(end:-1:1)], grayColor, 'EdgeColor', 'none');
hold on

p1 = plot(Ntime*100, y1,'k','LineWidth',1.5);
hold on
p2 = plot(Ntime*100, y3,'LineWidth',1.5, 'Color', Color_9(Idx_Acts_9Groups(MN),:));
hold on

xl = xline((1-MotionData.GenericCat.DutyFactor.Average)*100,':');
xl.LineWidth = 2;
legend([p1 pp p2], 'Mean EMG', 'STD EMGs','Act from 9');
title(MuscleNames_9Groups(MN))
% xlabel('Normalized cycle time, %')
ylabel('Act')
% set(gca,'XTick',[])
ytickformat('%.2f')
ylim([0 max([max(y3) max(y1_up)])])
box on
R4 = corrcoef(EMG_adj_mean{Idx_EMGs(MN), 1}, Activations{Idx_Acts(MN)}.a)



subplot(3,3,6)
MN = 6; % based on EMGs
y1 = EMG_adj_mean{Idx_EMGs(MN), 1};
y2 = Activations{Idx_Acts(MN)}.a;
y3 = Activations_9Groups{Idx_Acts_9Groups(MN)}.a;
y4 = EMG_adj{Idx_EMGs(MN), 1};

STD = std(y4')';
y1_up = y1+STD;
y1_down = y1-STD;
pp = patch([Ntime*100; Ntime(end:-1:1)*100], [y1_down ;y1_up(end:-1:1)], grayColor, 'EdgeColor', 'none');
hold on

p1 = plot(Ntime*100, y1,'k','LineWidth',1.5);
hold on
p2 = plot(Ntime*100, y3,'LineWidth',1.5, 'Color', Color_9(Idx_Acts_9Groups(MN),:));
hold on

xl = xline((1-MotionData.GenericCat.DutyFactor.Average)*100,':');
xl.LineWidth = 2;
legend([p1 pp p2], 'Mean EMG', 'STD EMGs','Act from 9');
title(MuscleNames_9Groups(MN))
% xlabel('Normalized cycle time, %')
ylabel('Act')
% set(gca,'XTick',[])
ytickformat('%.2f')
ylim([0 max([max(y3) max(y1_up)])])
box on
R4 = corrcoef(EMG_adj_mean{Idx_EMGs(MN), 1}, Activations{Idx_Acts(MN)}.a)



subplot(3,3,7)
MN = 7; % based on EMGs
y1 = EMG_adj_mean{Idx_EMGs(MN), 1};
y2 = Activations{Idx_Acts(MN)}.a;
y3 = Activations_9Groups{Idx_Acts_9Groups(MN)}.a;
y4 = EMG_adj{Idx_EMGs(MN), 1};

STD = std(y4')';
y1_up = y1+STD;
y1_down = y1-STD;
pp = patch([Ntime*100; Ntime(end:-1:1)*100], [y1_down ;y1_up(end:-1:1)], grayColor, 'EdgeColor', 'none');
hold on

p1 = plot(Ntime*100, y1,'k','LineWidth',1.5);
hold on
p2 = plot(Ntime*100, y3,'LineWidth',1.5, 'Color', Color_9(Idx_Acts_9Groups(MN),:));
hold on

xl = xline((1-MotionData.GenericCat.DutyFactor.Average)*100,':');
xl.LineWidth = 2;
legend([p1 pp p2], 'Mean EMG', 'STD EMGs','Act from 9');
title(MuscleNames_9Groups(MN))
% xlabel('Normalized cycle time, %')
ylabel('Act')
% set(gca,'XTick',[])
ytickformat('%.2f')
ylim([0 max([max(y3) max(y1_up)])])
box on
R4 = corrcoef(EMG_adj_mean{Idx_EMGs(MN), 1}, Activations{Idx_Acts(MN)}.a)



subplot(3,3,8)
MN = 9; % based on EMGs (TJ) -> Elbow flexor
y1_1 = EMG_adj_mean{Idx_EMGs(MN), 1};
y2_1 = Activations{Idx_Acts(MN)}.a;
y3_1 = Activations_9Groups{Idx_Acts_9Groups(MN)}.a;
y4_1 = EMG_adj{Idx_EMGs(MN), 1};

MN = 11; % based on EMGs (SD) -> Elbow flexor
y1_2 = EMG_adj_mean{Idx_EMGs(MN), 1};
y2_2 = Activations{Idx_Acts(MN)}.a;
y3_2 = Activations_9Groups{Idx_Acts_9Groups(MN)}.a;
y4_2 = EMG_adj{Idx_EMGs(MN), 1};

y1 = mean([y1_1,y1_2], 2);
if y3_1==y3_2; y3= y3_1; end
y4 = [y4_1, y4_2];

STD = std(y4')';
y1_up = y1+STD;
y1_down = y1-STD;
pp = patch([Ntime*100; Ntime(end:-1:1)*100], [y1_down ;y1_up(end:-1:1)], grayColor, 'EdgeColor', 'none');
hold on

p1 = plot(Ntime*100, y1,'k','LineWidth',1.5);
hold on
p2 = plot(Ntime*100, y3,'LineWidth',1.5, 'Color', Color_9(Idx_Acts_9Groups(MN),:));
hold on

xl = xline((1-MotionData.GenericCat.DutyFactor.Average)*100,':');
xl.LineWidth = 2;
legend([p1 pp p2], 'Mean EMG', 'STD EMGs','Act from 9');
title(MuscleNames_9Groups(MN))
% xlabel('Normalized cycle time, %')
ylabel('Act')
% set(gca,'XTick',[])
ytickformat('%.2f')
ylim([0 max([max(y3) max(y1_up)])])
box on
R4 = corrcoef(EMG_adj_mean{Idx_EMGs(MN), 1}, Activations{Idx_Acts(MN)}.a)






subplot(3,3,9)
MN = 10; % based on EMGs
y1 = EMG_adj_mean{Idx_EMGs(MN), 1};
% y2 = Activations{Idx_Acts(MN)}.a;
% y3 = Activations_9Groups{Idx_Acts_9Groups(MN)}.a;
y4 = EMG_adj{Idx_EMGs(MN), 1};
hold on

yyaxis right
STD = std(y4')';
y1_up = y1+STD;
y1_down = y1-STD;
pp = patch([Ntime*100; Ntime(end:-1:1)*100], [y1_down; y1_up(end:-1:1)], grayColor, 'EdgeColor', 'none');
hold on
% pp.Color(4) = 0.15; % transparent
p1 = plot(Ntime*100, y1,'-k','LineWidth',2);
ylim([0 1])
ax = gca;
ax.YAxis(2).Color = [0 0 0];
ax.YAxis(2).LineWidth = 2;
ax.YAxis(2). FontWeight = 'bold';
% p2 = plot(Ntime*100, y3,'LineWidth',1.5, 'Color', Color_9(Idx_Acts_9Groups(MN),:));
ylabel('EMGs')
hold on

yyaxis left
ax = gca;
ax.YAxis(1).Color = [0 0 0];
ax.YAxis(1).LineWidth = 1;
ax.YAxis(1).Visible='off'; % Removes left axis

% p3 = plot(Ntime*100, y3,'-.b','LineWidth',1.5);
xl = xline((1-MotionData.GenericCat.DutyFactor.Average)*100,':');
xl.LineWidth = 2;
%legend([p1 pp], 'Mean EMG', 'All EMGs');
title(MuscleNames_9Groups(MN))
% xlabel('Normalized cycle time, %')
ylabel('Act')
% set(gca,'XTick',[])
ytickformat('%.2f')
ylim([0 max(max(y4))])
box on




x0=50;
y0=50;
width=1800;
height=1000;
set(gcf,'position',[x0,y0,width,height])
exportgraphics(gcf,'FigEMGs_RepresentativeMuscles.pdf','ContentType','vector')




%% figure 2


figure(2)

grayColor = [.7 .7 .71];


subplot(6,1,1)
MN = 1; % based on EMGs
y1 = EMG_adj_mean{Idx_EMGs(MN), 1};
y2 = Activations{Idx_Acts(MN)}.a;
y3 = Activations_9Groups{Idx_Acts_9Groups(MN)}.a;
y4 = EMG_adj{Idx_EMGs(MN), 1};

STD = std(y4')';
y1_up = y1+STD;
y1_down = y1-STD;
pp = patch([Ntime*100; Ntime(end:-1:1)*100], [y1_down; y1_up(end:-1:1)], grayColor, 'EdgeColor', 'none');
hold on

p1 = plot(Ntime*100, y1,'k','LineWidth',1.5);
hold on
p2 = plot(Ntime*100, y3,'LineWidth',1.5, 'Color', Color_9(Idx_Acts_9Groups(MN),:));
hold on

xl = xline((1-MotionData.GenericCat.DutyFactor.Average)*100,':');
xl.LineWidth = 2;
legend([p1 pp p2], 'Mean EMG', 'STD EMGs','Act from 9');
title(MuscleNames_9Groups(MN))
% xlabel('Normalized cycle time, %')
ylabel('Act')
% set(gca,'XTick',[])
ytickformat('%.2f')
mm = max([max(y3) max(y1_up)]);
ylim([0 mm])
yticks([0 mm*1/2 mm*2/2])
box on
R4 = corrcoef(EMG_adj_mean{Idx_EMGs(MN), 1}, Activations{Idx_Acts(MN)}.a)


subplot(6,1,2)
MN = 2; % based on EMGs
y1 = EMG_adj_mean{Idx_EMGs(MN), 1};
y2 = Activations{Idx_Acts(MN)}.a;
y3 = Activations_9Groups{Idx_Acts_9Groups(MN)}.a;
y4 = EMG_adj{Idx_EMGs(MN), 1};

STD = std(y4')';
y1_up = y1+STD;
y1_down = y1-STD;
pp = patch([Ntime*100; Ntime(end:-1:1)*100], [y1_down ;y1_up(end:-1:1)], grayColor, 'EdgeColor', 'none');
hold on

p1 = plot(Ntime*100, y1,'k','LineWidth',1.5);
hold on
p2 = plot(Ntime*100, y3,'LineWidth',1.5, 'Color', Color_9(Idx_Acts_9Groups(MN),:));
hold on

xl = xline((1-MotionData.GenericCat.DutyFactor.Average)*100,':');
xl.LineWidth = 2;
%legend([p1 pp p2], 'Mean EMG', 'STD EMGs','Act from 9');
title(MuscleNames_9Groups(MN))
% xlabel('Normalized cycle time, %')
ylabel('Act')
% set(gca,'XTick',[])
ytickformat('%.2f')
mm = max([max(y3) max(y1_up)]);
ylim([0 mm])
yticks([0 mm*1/2 mm*2/2])
box on
R4 = corrcoef(EMG_adj_mean{Idx_EMGs(MN), 1}, Activations{Idx_Acts(MN)}.a)



subplot(6,1,3)
MN = 4; % based on EMGs (PT) -> Elbow flexor
y1_1 = EMG_adj_mean{Idx_EMGs(MN), 1};
y2_1 = Activations{Idx_Acts(MN)}.a;
y3_1 = Activations_9Groups{Idx_Acts_9Groups(MN)}.a;
y4_1 = EMG_adj{Idx_EMGs(MN), 1};

MN = 8; % based on EMGs (Br) -> Elbow flexor
y1_2 = EMG_adj_mean{Idx_EMGs(MN), 1};
y2_2 = Activations{Idx_Acts(MN)}.a;
y3_2 = Activations_9Groups{Idx_Acts_9Groups(MN)}.a;
y4_2 = EMG_adj{Idx_EMGs(MN), 1};

y1 = mean([y1_1,y1_2], 2);
if y3_1==y3_2; y3= y3_1; end
y4 = [y4_1, y4_2];
hold on;

STD = std(y4')';
y1_up = y1+STD;
y1_down = y1-STD;
pp = patch([Ntime*100; Ntime(end:-1:1)*100], [y1_down ;y1_up(end:-1:1)], grayColor, 'EdgeColor', 'none');
hold on

p1 = plot(Ntime*100, y1,'k','LineWidth',1.5);
hold on
p2 = plot(Ntime*100, y3,'LineWidth',1.5, 'Color', Color_9(Idx_Acts_9Groups(MN),:));
hold on

xl = xline((1-MotionData.GenericCat.DutyFactor.Average)*100,':');
xl.LineWidth = 2;
%legend([p1 pp p2], 'Mean EMG', 'STD EMGs','Act from 9');
title(MuscleNames_9Groups(MN))
% xlabel('Normalized cycle time, %')
ylabel('Act')
% set(gca,'XTick',[])
ytickformat('%.2f')
mm = max([max(y3) max(y1_up)]);
ylim([0 mm])
yticks([0 mm*1/2 mm*2/2])
box on
R4 = corrcoef(EMG_adj_mean{Idx_EMGs(MN), 1}, Activations{Idx_Acts(MN)}.a)



subplot(6,1,4)
MN = 5; % based on EMGs
y1 = EMG_adj_mean{Idx_EMGs(MN), 1};
y2 = Activations{Idx_Acts(MN)}.a;
y3 = Activations_9Groups{Idx_Acts_9Groups(MN)}.a;
y4 = EMG_adj{Idx_EMGs(MN), 1};

STD = std(y4')';
y1_up = y1+STD;
y1_down = y1-STD;
pp = patch([Ntime*100; Ntime(end:-1:1)*100], [y1_down ;y1_up(end:-1:1)], grayColor, 'EdgeColor', 'none');
hold on

p1 = plot(Ntime*100, y1,'k','LineWidth',1.5);
hold on
p2 = plot(Ntime*100, y3,'LineWidth',1.5, 'Color', Color_9(Idx_Acts_9Groups(MN),:));
hold on

xl = xline((1-MotionData.GenericCat.DutyFactor.Average)*100,':');
xl.LineWidth = 2;
%legend([p1 pp p2], 'Mean EMG', 'STD EMGs','Act from 9');
title(MuscleNames_9Groups(MN))
% xlabel('Normalized cycle time, %')
ylabel('Act')
% set(gca,'XTick',[])
ytickformat('%.2f')
mm = max([max(y3) max(y1_up)]);
ylim([0 mm])
yticks([0 mm*1/2 mm*2/2])
box on
R4 = corrcoef(EMG_adj_mean{Idx_EMGs(MN), 1}, Activations{Idx_Acts(MN)}.a)



subplot(6,1,5)
MN = 6; % based on EMGs
y1 = EMG_adj_mean{Idx_EMGs(MN), 1};
y2 = Activations{Idx_Acts(MN)}.a;
y3 = Activations_9Groups{Idx_Acts_9Groups(MN)}.a;
y4 = EMG_adj{Idx_EMGs(MN), 1};

STD = std(y4')';
y1_up = y1+STD;
y1_down = y1-STD;
pp = patch([Ntime*100; Ntime(end:-1:1)*100], [y1_down ;y1_up(end:-1:1)], grayColor, 'EdgeColor', 'none');
hold on

p1 = plot(Ntime*100, y1,'k','LineWidth',1.5);
hold on
p2 = plot(Ntime*100, y3,'LineWidth',1.5, 'Color', Color_9(Idx_Acts_9Groups(MN),:));
hold on

xl = xline((1-MotionData.GenericCat.DutyFactor.Average)*100,':');
xl.LineWidth = 2;
%legend([p1 pp p2], 'Mean EMG', 'STD EMGs','Act from 9');
title(MuscleNames_9Groups(MN))
% xlabel('Normalized cycle time, %')
ylabel('Act')
% set(gca,'XTick',[])
ytickformat('%.2f')
mm = max([max(y3) max(y1_up)]);
ylim([0 mm])
yticks([0 mm*1/2 mm*2/2])
box on
R4 = corrcoef(EMG_adj_mean{Idx_EMGs(MN), 1}, Activations{Idx_Acts(MN)}.a)



subplot(6,1,6)
MN = 7; % based on EMGs
y1 = EMG_adj_mean{Idx_EMGs(MN), 1};
y2 = Activations{Idx_Acts(MN)}.a;
y3 = Activations_9Groups{Idx_Acts_9Groups(MN)}.a;
y4 = EMG_adj{Idx_EMGs(MN), 1};

STD = std(y4')';
y1_up = y1+STD;
y1_down = y1-STD;
pp = patch([Ntime*100; Ntime(end:-1:1)*100], [y1_down ;y1_up(end:-1:1)], grayColor, 'EdgeColor', 'none');
hold on

p1 = plot(Ntime*100, y1,'k','LineWidth',1.5);
hold on
p2 = plot(Ntime*100, y3,'LineWidth',1.5, 'Color', Color_9(Idx_Acts_9Groups(MN),:));
hold on

xl = xline((1-MotionData.GenericCat.DutyFactor.Average)*100,':');
xl.LineWidth = 2;
%legend([p1 pp p2], 'Mean EMG', 'STD EMGs','Act from 9');
title(MuscleNames_9Groups(MN))
% xlabel('Normalized cycle time, %')
ylabel('Act')
% set(gca,'XTick',[])
ytickformat('%.2f')
mm = max([max(y3) max(y1_up)]);
ylim([0 mm])
yticks([0 mm*1/2 mm*2/2])
box on
R4 = corrcoef(EMG_adj_mean{Idx_EMGs(MN), 1}, Activations{Idx_Acts(MN)}.a)



x0=50;
y0=50;
width=400;
height=1000;
set(gcf,'position',[x0,y0,width,height])
exportgraphics(gcf,'FigEMGs_RepresentativeMuscles_Vertical.pdf','ContentType','vector')








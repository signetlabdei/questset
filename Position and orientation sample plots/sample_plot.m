% Read CSV file

opts = detectImportOptions("sample_movement_data.csv",'NumHeaderLines',0);
data = readtable("sample_movement_data.csv",opts);

% Extract postion and orientation information for the headset

posX = data.HeadPosX;
posY = data.HeadPosY;
posZ = data.HeadPosZ;
w = data.HeadOrientationW;
x = data.HeadOrientationX;
y = data.HeadOrientationY;
z = data.HeadOrientationZ;
time = data.time;

%Convert from quaternions to euler angles
q = [w, z, x, y];
[yaw, pitch, roll]=quat2angle(q);
% Convert to degrees
yaw_deg=rad2deg(yaw);
pitch_deg=rad2deg(pitch);
roll_deg=rad2deg(roll);

% Plot the figures

figure1 = figure;
axes1 = axes('Parent',figure1);
hold(axes1,'on');
plot1 = plot(time,[roll_deg,pitch_deg,yaw_deg],'LineWidth',2,'Parent',axes1);
set(plot1(1),'DisplayName','roll','Color',[0 0.447058826684952 0.74117648601532]);
set(plot1(2),'DisplayName','pitch','Color',[1 0.600000023841858 0]);
set(plot1(3),'DisplayName','yaw','Color',[0 0.800000011920929 0.200000002980232]);
box(axes1,'on');
hold(axes1,'off');
legend(axes1,'show');
xlabel({'Time [s]'});
ylabel('Rotation angles [deg]')

figure2 = figure;
axes2 = axes('Parent',figure2);
hold(axes2,'on');
plot2 = plot(time,[posZ,posX,posY],'LineWidth',2,'Parent',axes2);
set(plot2(1),'DisplayName','z','Color',[0 0.447058826684952 0.74117648601532]);
set(plot2(3),'DisplayName','y','Color',[0 0.800000011920929 0.200000002980232]);
set(plot2(2),'DisplayName','x','Color',[1 0.600000023841858 0]);
box(axes2,'on');
hold(axes2,'off');
legend(axes2,'show');
xlabel({'Time [s]'});
ylabel('Position [m]')
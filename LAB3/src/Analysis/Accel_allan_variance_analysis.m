data = readmatrix('/home/rayyan/catkin_ws/EECE5554/LAB3/src/Analysis/imu.csv');

AccelX = data(:, 4);
AccelY = data(:, 5); 
AccelZ = data(:, 6); 

Fs=40;
t0=1/Fs;

accel_x=cumsum(AccelX, 1)*t0;
accel_y=cumsum(AccelY, 1)*t0;
accel_z=cumsum(AccelZ, 1)*t0;

max_num = 100;

Lx = size(accel_x, 1);
Ly = size(accel_y, 1);
Lz = size(accel_z, 1);

max_m_x = 2.^floor(log2(Lx/2));
max_m_y = 2.^floor(log2(Ly/2));
max_m_z = 2.^floor(log2(Lz/2));

mx = logspace(log10(1), log10(max_m_x), max_num).';
my = logspace(log10(1), log10(max_m_y), max_num).';
mz = logspace(log10(1), log10(max_m_z), max_num).';

mx = ceil(mx); % m must be an integer.
mx = unique(mx); % Remove duplicates.

my = ceil(my); % m must be an integer.
my = unique(my); % Remove duplicates.

mz = ceil(mz); % m must be an integer.
mz = unique(mz); % Remove duplicates.

taux = mx*t0;
tauy = my*t0;
tauz = mz*t0;

avarx = zeros(numel(mx), 1);
avary = zeros(numel(my), 1);
avarz = zeros(numel(mz), 1);

for i = 1:numel(mx)
    mi = mx(i);
    avarx(i,:) = sum( ...
        (accel_x(1+2*mi:Lx) - 2*accel_x(1+mi:Lx-mi) + accel_x(1:Lx-2*mi)).^2, 1);
end
avarx = avarx ./ (2*taux.^2 .* (Lx - 2*mx));
adevx = sqrt(avarx);

for i = 1:numel(my)
    mi = my(i);
    avary(i,:) = sum( ...
        (accel_y(1+2*mi:Ly) - 2*accel_y(1+mi:Ly-mi) + accel_y(1:Ly-2*mi)).^2, 1);
end
avary = avary ./ (2*tauy.^2 .* (Ly - 2*my));
adevy = sqrt(avary);

for i = 1:numel(mz)
    mi = mz(i);
    avarz(i,:) = sum( ...
        (accel_z(1+2*mi:Lz) - 2*accel_z(1+mi:Lz-mi) + accel_z(1:Lz-2*mi)).^2, 1);
end
avarz = avarz ./ (2*tauz.^2 .* (Lz - 2*mz));
adevz = sqrt(avarz);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
slopex1 = -0.5;
logtaux1 = log10(taux);
logadevx1 = log10(adevx);
dlogadevx1 = diff(logadevx1) ./ diff(logtaux1);
[~, ix1] = min(abs(dlogadevx1 - slopex1));

% Find the y-intercept of the line.
bx1 = logadevx1(i) - slopex1*logtaux1(i);

% Determine the angle random walk coefficient from the line.
logNx1 = slopex1*log(1) + bx1;
Nx1 = 10^logNx1

tauNx1 = 1;
lineNx1 = Nx1 ./ sqrt(taux);

% Find the index where the slope of the log-scaled Allan deviation is equal
% to the slope specified.
slopex2 = 0.5;
logtaux2 = log10(taux);
logadevx2 = log10(adevx);
dlogadevx2 = diff(logadevx2) ./ diff(logtaux2);
[~, ix2] = min(abs(dlogadevx2 - slopex2));

% Find the y-intercept of the line.
bx2 = logadevx2(ix2) - slopex2*logtaux2(ix2);

% Determine the rate random walk coefficient from the line.
logKx2 = slopex2*log10(3) + bx2;
Kx2 = 10^logKx2

% Plot the results.
tauKx2 = 3;
lineKx2 = Kx2 .* sqrt(taux/3);

slopex3 = 0;
logtaux3 = log10(taux);
logadevx3 = log10(adevx);
dlogadevx3 = diff(logadevx3) ./ diff(logtaux3);
[~, ix3] = min(abs(dlogadevx3 - slopex3));

% Find the y-intercept of the line.
bx3 = logadevx3(ix3) - slopex3*logtaux3(ix3);

% Determine the bias instability coefficient from the line.
scfBx3 = sqrt(2*log(2)/pi);
logBx3 = bx3 - log10(scfBx3);
Bx3 = 10^logBx3

% % Plot the results
tauBx3 = taux(ix3);
lineBx3 = Bx3 * scfBx3 * ones(size(taux));


tauParamsx = [tauNx1, tauKx2, tauBx3];
paramsx = [Nx1, Kx2, scfBx3*Bx3];
figure
loglog(taux, adevx, taux, [lineNx1, lineKx2, lineBx3], '--', ...
    tauParamsx, paramsx, 'o')
title('Allan Deviation in Accel X with Noise Parameters')
xlabel('\tau')
ylabel('\sigma(\tau)')
legend('$\sigma (rad/s)$', '$\sigma (rad/s)$', '$\sigma_N ((rad/s)/\sqrt{Hz})$', ...
    '$\sigma_K ((rad/s)\sqrt{Hz})$', '$\sigma_B (rad/s)$', 'Interpreter', 'latex')
text(tauParamsx, paramsx, {'N', 'K', '0.664B'})
grid on
axis equal

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
slopey1 = -0.5;
logtauy1 = log10(tauy);
logadevy1 = log10(adevy);
dlogadevy1 = diff(logadevy1) ./ diff(logtauy1);
[~, iy1] = min(abs(dlogadevy1 - slopey1));

% Find the y-intercept of the line.
by1 = logadevy1(iy1) - slopey1*logtauy1(iy1);

% Determine the angle random walk coefficient from the line.
logNy1 = slopey1*log(1) + by1;
Ny1 = 10^logNy1

tauNy1 = 1;
lineNy1 = Ny1 ./ sqrt(tauy);

% Find the index where the slope of the log-scaled Allan deviation is equal
% to the slope specified.
slopey2 = 0.5;
logtauy2 = log10(tauy);
logadevy2 = log10(adevy);
dlogadevy2 = diff(logadevy2) ./ diff(logtauy2);
[~, iy2] = min(abs(dlogadevy2 - slopey2));

% Find the y-intercept of the line.
by2 = logadevy2(iy2) - slopey2*logtauy2(iy2);

% Determine the rate random walk coefficient from the line.
logKy2 = slopey2*log10(3) + by2;
Ky2 = 10^logKy2

% Plot the results.
tauKy2 = 3;
lineKy2 = Ky2 .* sqrt(tauy/3);

slopey3 = 0;
logtauy3 = log10(tauy);
logadevy3 = log10(adevy);
dlogadevy3 = diff(logadevy3) ./ diff(logtauy3);
[~, iy3] = min(abs(dlogadevy3 - slopey3));

% Find the y-intercept of the line.
by3 = logadevy3(iy3) - slopey3*logtauy3(iy3);

% Determine the bias instability coefficient from the line.
scfBy3 = sqrt(2*log(2)/pi);
logBy3 = by3 - log10(scfBy3);
By3 = 10^logBy3

% % Plot the results.
tauBy3 = tauy(iy3);
lineBy3 = By3 * scfBy3 * ones(size(tauy));


tauParamsy = [tauNy1, tauKy2, tauBy3];
paramsy = [Ny1, Ky2, scfBy3*By3];
figure
loglog(tauy, adevy, tauy, [lineNy1, lineKy2, lineBy3], '--', ...
    tauParamsy, paramsy, 'o')
title('Allan Deviation in Accel Y with Noise Parameters')
xlabel('\tau')
ylabel('\sigma(\tau)')
legend('$\sigma $', '$\sigma_N $', ...
    '$\sigma_K $', '$\sigma_B $', 'Interpreter', 'latex')
text(tauParamsy, paramsy, {'N', 'K', '0.664B'})
grid on
axis equal

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
slopez1 = -0.5;
logtauz1 = log10(tauz);
logadevz1 = log10(adevz);
dlogadevz1 = diff(logadevz1) ./ diff(logtauz1);
[~, iz1] = min(abs(dlogadevz1 - slopez1));

% Find the y-intercept of the line.
bz1 = logadevz1(iz1) - slopez1*logtauz1(iz1);

% Determine the angle random walk coefficient from the line.
logNz1 = slopez1*log(1) + bz1;
Nz1 = 10^logNz1

tauNz1 = 1;
lineNz1 = Nz1 ./ sqrt(tauz);

% Find the index where the slope of the log-scaled Allan deviation is equal
% to the slope specified.
slopez2 = 0.5;
logtauz2 = log10(tauz);
logadevz2 = log10(adevz);
dlogadevz2 = diff(logadevz2) ./ diff(logtauz2);
[~, iz2] = min(abs(dlogadevz2 - slopez2));

% Find the y-intercept of the line.
bz2 = logadevz2(iz2) - slopez2*logtauz2(iz2);

% Determine the rate random walk coefficient from the line.
logKz2 = slopez2*log10(3) + bz2;
Kz2 = 10^logKz2

% Plot the results.
tauKz2 = 3;
lineKz2 = Kz2 .* sqrt(tauz/3);

slopez3 = 0;
logtauz3 = log10(tauz);
logadevz3 = log10(adevz);
dlogadevz3 = diff(logadevz3) ./ diff(logtauz3);
[~, iz3] = min(abs(dlogadevz3 - slopez3));

% Find the y-intercept of the line.
bz3 = logadevz3(iz3) - slopez3*logtauz3(iz3);

% Determine the bias instability coefficient from the line.
scfBz3 = sqrt(2*log(2)/pi);
logBz3 = bz3 - log10(scfBz3);
Bz3 = 10^logBz3

% % Plot the results.
tauBz3 = tauz(iz3);
lineBz3 = Bz3 * scfBz3 * ones(size(tauz));


tauParamsz = [tauNz1, tauKz2, tauBz3];
paramsz = [Nz1, Kz2, scfBz3*Bz3];
figure
loglog(tauz, adevz, tauz, [lineNz1, lineKz2, lineBz3], '--', ...
    tauParamsz, paramsz, 'o')
title('Allan Deviation in Accel Z with Noise Parameters')
xlabel('\tau')
ylabel('\sigma(\tau)')
legend('$\sigma$', '$\sigma_N $', ...
    '$\sigma_K $', '$\sigma_B $', 'Interpreter', 'latex')
text(tauParamsz, paramsz, {'N', 'K', '0.664B'})
grid on
axis equal

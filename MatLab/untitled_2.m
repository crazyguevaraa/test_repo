%Изучение красного смещения звезд 
close all 
clear variables 

%Импорт данных 
spectra = importdata('spectra.csv'); 
lambdaStart = importdata('lambda_start.csv'); 
lambdaDelta = importdata('lambda_delta.csv'); 
starNames = importdata("star_names.csv"); 

%Константы 
lambdaPr = 656.28; %нм 
speedOfLight = 299792.458; %км/c 
numberObs = size(spectra, 1); 
nStars = size(starNames,1 ); 

%Определение диапазона длин волн 
lambdaEnd = lambdaStart + (numberObs - 1) * lambdaDelta; 
lambda = (lambdaStart : lambdaDelta : lambdaEnd)'; 

%Расчет скорости удаления от Земли 
for counter1 = 1 : nStars 
s = spectra(:, counter1); 
[sHa, idx] = min(s); 
lambdaHa = lambda(idx); 
z = (lambdaHa / lambdaPr) - 1; % Если z > 0 => красное 
speed(counter1) = z * speedOfLight; 
%speed = speed'; 
end 
speed = speed'; 
movaway = starNames(speed > 0) 

%Построение графика 
fg1 = figure; 
hold on 
for counter = 1 : nStars 
s = spectra(:, counter); 
[sHa, idx] = min(s); 
lambdaHa = lambda(idx); 
if ( speed(counter) > 0 ) 
plot(lambda, s, 'LineWidth', 3, 'Color', [0.2 0.8 0.7]); 
end 
if ( speed(counter) < 0 ) 
plot(lambda, s,'--', 'LineWidth', 1, 'Color', [0.9 0.1 0.1]); 
end 
set(fg1, 'visible', 'on'); 
end 
hold off 
grid on 
xlabel('Длина волны, мм'); 
ylabel(['Интенсивность, эрг/см^2/с/', char(197)]); 
title('Спектры звезд'); 
legend(starNames); 
text(lambdaEnd - 47, max(s)*8, ['Puchkov Danila, Б01-006']); 

%Сохранение графика 
saveas(fg1, 'spectras.png')
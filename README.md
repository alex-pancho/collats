Формулировка задачи
Правила для числового ряда:
1. для нечётных чисел - 
2. для четных чисел - 
Гипотеза Коллатца:
любое n придет к циклу 4-2-1.



Документ на гугль-драйве:
https://docs.google.com/document/d/1I_K6teGB7hTyGXtQ23FjI-8VCqVDHJQF1EbO7kgwJwE/edit?usp=sharing


   1.  Доказательство для всех 2^x
если число n – степень числа 2, оно всегда достигнет 2 с x-1 шагов деления
(2,4,8,16,32,64,128,256,512,1024, 2048, 4096… )

   2. Правило для всех четных чисел, вне множества 2^x
четные, не являющиеся степенью двойки через конечное количество операций деления уменьшаются до нечетных.
Отсюда следует, что имеет смысл рассматривать только поведение множества нечётных чисел - odd  (от англ. odd - нечетные).

   3. Нечётные числа - делители числа 3
нечётные делители 3 (odd//3==0) достигают 2 за конечное число нечетных odd. 

Линия доказательств 1
Для  odd <= 3^3, образуется замкнутая на 5 зона разложения:

3*1 = 3+1 = 4/2 = 2

3*3 = 9+1 = 10/2 = 5

3*5 = 15+1 = 16 = (2^4)

3*7 = 21+1 = 22/2 = 11

3*9 = 27+1 = 28/2 = 14/2 = 7

3*11 = 33+1 = 34/2 = 17

3*13 = 39+1 = 40/2 = 20/2 = 10/2 = 5

3*17 = 51+1 = 52/2 = 26/2= 13


упростим запись, оставив только начальное число и результат:

1 → 2

3 → 5

5 → (2^4)

7 → 11

9 → 7

11 → 17

13 → 5

17 → 13



продолжим ряды по заданным правилам:

3 → 5 → (2^4)

5 → (2^4)

7 → 11 → 17 → 13 → 5 → (2^4)

9 → 7 → 11 → 17 → 13 → 5 → (2^4)

11 → 17 → 13 → 5 → (2^4)

13 → 5 → (2^4)

17 → 13 → 5 → (2^4)


Фактически, для части формулы 3n+1,   для n = odd//3 =0, мы просто получаем следующий делитель числа 3.


Иллюстрация на примере числа 21:

3*21 = 63+1 = 64 (2^6) → 2

или

21/3 = 7  → (...) → 5  → (2^4)



Иллюстрация на примере числа  15:

3*15 = 45+1 = 46/2 = 23

3*23 = 69+1 = 70/2 = 49

3*49 = 147+1 = 148/2 = 74/2 = 37

3*37 = 111+1 = 112/2 = 56/2 = 28/2 = 14/2 = 7

сократим запись:

15 → 23 → 49 → 37 → 7 → (...) → 5 → (2^4)

или

15/3 = 5 → (2^4)


Иллюстрация на примере числа  27:

3*27 = 81+1 = 82/2 = 41

3*41 = 123+1 = 124/2 = 62/2 = 31

и т.д. - 41 шаг:

27 →  41 →  31 →  47 →  71 →  107 →  161 →  121 →  91 →  137 →  103 →  155 →  233 →  175 →  263 →  395 →  593 →  445 →  167 →  251 →  377 →  283 →  425 →  319 →  479 →  719 →  1079 →  1619 →  2429 →  911 →  1367 →  2051 →  3077 →  577 →  433 →  325 →  61 →  23 →  35 →  53 →  5 → (2^4)

или:

27/3 = 9/3 = 3/3  =  1



Линия доказательств 2

все четные v, являющееся  степенью числа 2 можно представить как 3n+1, где n = odd//3 = 0

(2^2) = 4-1 = 3(/3 =1)

(2^4) = 16-1 = 15(/3 = 5)

(2^6) = 64-1 = 63(/3 = 21/3 = 7)

(2^8) = 256-1 = 255(/3 = 85/3 = 7)

(2^10) = 64-1 = 63(/3 = 21/3 = 7)

и т.д, например

(2^200) = 401734511064747568885490523085290650630550748445698208825344-1 = 401734511064747568885490523085290650630550748445698208825343/3 = 133911503688249189628496841028430216876850249481899402941781


   4. Нечётные числа не делящиеся на  3
   
(не написано)
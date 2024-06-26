# Сортировка выбором

Сортировка выбором - улучшенная сортировка пузырьком. 

За каждый проход выполняется один обмен (сравните с N – 1 в случае сортировки пузырьком). Вместо того чтобы перемещать наибольшее значение маленькими шагами, мы ищем его на каждой 
итерации и ставим в конец списка. 

Это значит, что в результате первого прохода наибольшее значение окажется справа, а в результате второго прохода к нему переместится следующее по величине значение.

По мере выполнения алгоритма последующие элементы будут перемещаться в нужное место согласно их значению.

Последний элемент будет перемещен после (N – 1)-го прохода.

Таким образом, сортировка выбором требует N – 1 проходов для сортировки N элементов

## Анализ производительности сортировки выбором

Наихудшая производительность алгоритма сортировки выбором — O(N2), аналогично сортировке пузырьком. Поэтому его не следует использовать для обработки больших наборов данных. Тем не менее сортировка выбором — это более продуманный алгоритм, чем сортировка пузырьком, и его средняя производительность лучше из-за сокращения числа обменов значений.

Алгоритм сортировки выбором на Python выглядит так [>>>](select_sort.py)
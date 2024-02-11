# wine
1. Анализ качества вина по его химическому составу	
https://github.com/vl278/wine.git		
Dataset из kaggle	 (качество вина оценивается от 0 до 10)	
2. MapReduce. Average sugar for quality.

cat winequality-red.csv| python3 wineMap.py|sort|python3 wineReduce.py
quality = 3 average sugar=2.635 count=10
quality = 4 average sugar=2.69433962264151 count=53
quality = 5 average sugar=2.528854625550656 count=681
quality = 6 average sugar=2.477194357366766 count=638
quality = 7 average sugar=2.7206030150753766 count=199
quality = 8 average sugar=2.577777777777778 count=18


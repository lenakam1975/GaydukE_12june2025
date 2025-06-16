-- 1. Выберите уникальные регионы сбора грибов.
SELECT DISTINCT name
FROM Regions;

-- 2. Выведите название, сезон сбора и съедобность грибов, которые относятся к категории «Трубчатые».

SELECT mh.name_mushrooms, mh.season, mh.edible
FROM Mushrooms AS mh
JOIN Categories AS ct
on mh.category_id = ct.category_id
WHERE ct.name = 'трубчатые'

-- 3. Посчитайте количество грибов для каждой категории. 
-- Выведите название категории и количество в порядке убывания.

SELECT ct.name, count(mushroom_id)
FROM Categories AS ct
JOIN Mushrooms AS mh
on ct.category_id = mh.category_id
GROUP by ct.name
ORDER by count(mushroom_id)DESC

-- 4. Выведите название и описание съедобных грибов, 
-- которые лучше всего собирать в пяти самых больших по размеру (size) регионах.

SELECT mh.name_mushrooms, mh.description
FROM Mushrooms AS mh
JOIN Regions AS rg
on mh.region_id = rg.region_id
WHERE mh.edible = true
AND rg.size IN (
	SELECT size
	FROM Regions
	ORDER by size DESC
	LIMIT 5
);

-- 5. Выведите названия всех грибов, которые растут весной, относятся к категории «Пластинчатые» 
-- и которые лучше всего собирать в местах размером до 6000 условных единиц (size).

SELECT mh.name_mushrooms                     
FROM Mushrooms AS mh
JOIN Categories AS ct
on mh.category_id = ct.category_id
JOIN Regions AS rg
on mh.region_id = rg.region_id
WHERE mh.season = 'весна'
AND ct.name = 'пластинчатые'
AND rg.size < 6000;

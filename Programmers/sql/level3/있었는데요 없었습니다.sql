SELECT AI.ANIMAL_ID, AI.NAME 
FROM ANIMAL_INS as AI, ANIMAL_OUTS as AO
WHERE AI.ANIMAL_ID = AO.ANIMAL_ID AND AI.DATETIME > AO.DATETIME
ORDER BY AI.DATETIME
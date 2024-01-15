SELECT H.HISTORY_ID, 
    ROUND(C.DAILY_FEE * (DATEDIFF(H.END_DATE,H.START_DATE)+1)
    * (1 - 0.01 * (CASE 
        WHEN DATEDIFF(H.END_DATE, H.START_DATE)+1 < 7 
            THEN 0
        WHEN DATEDIFF(H.END_DATE, H.START_DATE)+1 < 30 
            THEN (SELECT DISCOUNT_RATE FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN WHERE CAR_TYPE="트럭" ORDER BY DISCOUNT_RATE LIMIT 1)
        WHEN DATEDIFF(H.END_DATE, H.START_DATE)+1 < 90 
            THEN (SELECT DISCOUNT_RATE FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN WHERE CAR_TYPE="트럭" ORDER BY DISCOUNT_RATE LIMIT 1 OFFSET 1)
        ELSE 
            (SELECT DISCOUNT_RATE FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN WHERE CAR_TYPE="트럭" ORDER BY DISCOUNT_RATE LIMIT 1 OFFSET 2) 
        END))) AS FEE
FROM CAR_RENTAL_COMPANY_CAR C
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H
ON C.CAR_ID = H.CAR_ID

WHERE C.CAR_TYPE = "트럭"
GROUP BY H.HISTORY_ID
ORDER BY FEE DESC , H.HISTORY_ID DESC
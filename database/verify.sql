-- Count reviews per bank
SELECT b.bank_name, COUNT(r.*) as review_count, ROUND(AVG(r.rating), 2) as avg_rating
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
GROUP BY b.bank_name
ORDER BY review_count DESC;

-- Sentiment distribution
SELECT bank_name, sentiment_label, COUNT(*) 
FROM reviews r JOIN banks b ON r.bank_id = b.bank_id
GROUP BY bank_name, sentiment_label;

-- Top 10 most negative reviews (for investigation)
SELECT bank_name, review_text, rating, sentiment_score
FROM reviews r JOIN banks b ON r.bank_id = b.bank_id
WHERE sentiment_label = 'negative'
ORDER BY sentiment_score ASC
LIMIT 10;
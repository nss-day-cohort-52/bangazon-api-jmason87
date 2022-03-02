            SELECT P.price, P.name ProductName, S.name StoreName
            FROM bangazon_api_product P
            JOIN bangazon_api_store S 
            ON P.store_id = S.id
            WHERE price > 1000

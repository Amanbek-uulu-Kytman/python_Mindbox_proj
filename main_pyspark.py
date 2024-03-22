from pyspark.sql.functions import col


def get_product_category_pairs(df_products, df_categories, df_relationships):
    joined_df = df_products.join(df_relationships, df_products["product_id"] == df_relationships["product_id"], "left") \
        .join(df_categories, df_relationships["category_id"] == df_categories["category_id"], "left")

    # Выберите столбцы для названия продукта, названия категории и отфильтруйте продукты без категорий.
    result_df = joined_df.select(df_products["product_name"], df_categories["category_name"]) \
        .filter(col("category_name").isNotNull()) \
        .orderBy("product_name")

    # Получить названия продуктов без категорий
    products_without_categories = df_products.join(df_relationships,
                                                   df_products["product_id"] == df_relationships["product_id"], "left") \
        .filter(col("category_id").isNull()) \
        .select("product_name") \
        .distinct()

    return result_df, products_without_categories

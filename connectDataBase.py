import psycopg2

connection = psycopg2.connect(
    host="127.0.0.1",
    user="postgres",
    password="qwerty",
    database="rkn_domain",
    port=5432)


def requestDataBase(domain_name):
    with connection.cursor() as cursor:
        cursor.execute(
            """
                SELECT ip
                FROM domain_main_tbl JOIN domain_ip_add
                ON id = domain_id
                WHERE domain = '{domain_name}'
                ORDER BY id;
            """.format(domain_name=domain_name)
        )

        output = cursor.fetchall()
        arr = set()
        for i in output:
            var = i[0]
            arr.add(var)
        return arr

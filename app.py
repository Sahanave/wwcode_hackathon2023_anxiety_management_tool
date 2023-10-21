import frontend.therapist_dashboard as first_dashboard
import setup.database as setup_db
import pandas as pd
def main():
    conn = setup_db.create_connection('aitool.db')
    setup_db.main()
    first_dashboard.main()
    conn.close()
 


if __name__ == '__main__':
    main()



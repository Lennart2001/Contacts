#done

def end_session(conn):
    if conn is not None:
        conn.close()
        print("Ended Session Successfully")
    else:
        print("Could not Close Session")



import psycopg2
import psycopg2.extras

from flask import Flask, request, make_response, jsonify

con = psycopg2.connect(
                host="localhost", 
                database="pet_hotel",
                user="postgres",
                password="postgres",
                cursor_factory=psycopg2.extras.RealDictCursor
)

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/pets', methods=['GET', 'POST'])

def gettingPosting():
    if (request.method == 'GET'):
        cur = con.cursor()
        queryText = "SELECT * FROM pets"
        cur.execute(queryText)
        records = cur.fetchall()
        cur.close()
        return jsonify(records), 201 

    elif (request.method == 'POST'):
        data = request.form
        # print(owner_name)
        cur = con.cursor()
        queryInsertText = "insert into owners (name) values (%s);"
        cur.execute(queryInsertText, (data["name"], ))
        con.commit()
        cur.close()
        return jsonify(data["name"]), 201





# @app.route(‘/pets/<id>’, methods=[‘PUT’, ‘DELETE’])

# def putDelete(id):
#     if (request.method == ‘PUT’):
#         cur = conn.cursor()
    
#         inOrOut = request.form[“check”]
#         if (inOrOut == ‘in’):
          
#             queryText = ‘UPDATE “pet” SET “checked_in” = TRUE WHERE id = %s;’
#             cur.execute(queryText, (id))
#             conn.commit()
#             cur.close()
#             return “checked in!“, 200
#         elif (inOrOut == ‘out’):
          
#             queryText = ‘UPDATE “pet” SET “checked_in” = FALSE WHERE id = %s;’
#             cur.execute(queryText, (id))
#             conn.commit()
#             cur.close()
#             return “checked out!“, 200
       
#     elif (request.method == ‘DELETE’):
#         cur = conn.cursor()
#         petId = id
#         queryText = (f’DELETE FROM “pet” WHERE id = {petId} RETURNING “pet”.pet_name;’)
#         cur.execute(queryText)
#         petName = cur.fetchall()
#         petName = petName[0]
#         print(“printing our thing”)
#         print(petName[‘pet_name’])
#         # conn.commit()
#         cur.close()
#         return jsonify(petName), 200

# if making put or delete req.params == request.args.get("name", "")

import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb+srv://challakrish:Krishnaveni@cluster0.xqhlz9j.mongodb.net/')


db = client['survey']


collection = db['users']


user_document = {
    'studentid': 'P8976',
    'name': 'KRITI',
    'gender': 'Female',
    'age': 22
     

}


def create_user(user):
    result = collection.insert_one(user)
    print(f'Inserted user with ID: {result.inserted_id}')


def read_users():
    users = collection.find()
    for user in users:
        print(user)


def read_user_by_studentid(studentid):
    user = collection.find_one({'studentid': studentid})
    print(user)


def update_user(studentid, updated_data):
    result = collection.update_one({'studentid': studentid}, {'$set': updated_data})
    if result.matched_count:
        print(f'Updated user with studentid: {studentid}')
    else:
        print(f'No user found with studentid: {studentid}')


def delete_user(studentid):
    result = collection.delete_one({'studentid': studentid})
    if result.deleted_count:
        print(f'Deleted user with studentid: {studentid}')
    else:
        print(f'No user found with studentid: {studentid}')

if __name__ == '__main__':

    # Insert a user
    create_user(user_document)

    #  Read all users
    print("All users:")
    read_users()

#     # Read a specific user by studentid
    print('User with studentid K3476:')
    read_user_by_studentid('K3476')

    # Update a user
    update_data = {'age': 30, 'name': 'PRITI'}
    update_user('K3476', update_data)
    
    # Read the updated user
    print("Updated user with studentid P8976:")
    read_user_by_studentid('P8976')

    # Delete the user
    delete_user('P8976')

    # Verify deletion
    print("All users after deletion:")
    read_users()




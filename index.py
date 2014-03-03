from bottle import run,get, post, request,delete,put
patient_record={}


  
@post('/patient/add_patient')
def add_new_patient():
    p_id = request.POST['id']
    p_name = request.POST['name']
    p_gender = request.POST['gender']
    p_age = request.POST['age']
    p_address = request.POST['address']
    p_phone = request.POST['phone']
    store_data={}
    store_data["Name"] = p_name
    store_data["Gender"] = p_gender
    store_data["Age"] = p_age
    store_data["Address"] = p_address
    store_data["Phone"] = p_phone
    patient_record.update({p_id:store_data})
    return patient_record

@get('/patient/display/<p_id>')
def show_patient_info(p_id):
    if p_id not in patient_record.keys():
        return 'Please enter correct patient id'
    else:
        return patient_record[p_id]

@put('/patient/update_info/<p_id>')
def update_patient_info(p_id):
    p_name = request.POST['name']
    p_gender = request.POST['gender']
    p_age = request.POST['age']
    p_address = request.POST['address']
    p_phone = request.POST['phone']
    store_data={}
    store_data["Name"] = p_name
    store_data["Gender"] = p_gender
    store_data["Age"] = p_age
    store_data["Address"] = p_address
    store_data["Phone"] = p_phone
    patient_record.update({p_id:store_data})
    return patient_record
   


@delete('/patient/delete_info/<p_id>')
def delete_patient_info(p_id):
    patient_record.pop(p_id)
    return patient_record


run(host='localhost',port=8080)

import uuid

uuids = {
    "bu_ass_uuid_executor":"",
    "ld_ass_uuid_writer":"",
    "ld_ass_uuid_executor":"",
    "co_ass_uuid_executor":"",
    "co_ass_uuid_writer": "",
    "ior_ass_uuid_executor":"",
    "stats_ass_uuid_executor":"", 
    "stats_ass_uuid_writer":"",
    "skew_ass_uuid_executor":"",
    "skew_ass_uuid_writer":"",
    "plaus_ass_uuid_executor" :"",
    "plaus_ass_uuid_writer":"",
    "vis_ass_uuid_executor" :  "",
    "vis_ass_uuid_writer":  "",
    "ass_uuid_executor_2e" : "", 
    "ass_uuid_writer_2e" : "",
    "ass_uuid_executor_2f" : "",
    "ass_uuid_writer_2f" : "" ,
    "ass_uuid_executor_2g" : "",
    "ass_uuid_writer_2g" : "" ,
    "ro_ass_uuid_executor" : "",
    "td_ass_uuid_writer" :  "",
    "fs_ass_uuid_executor" : "",
    "fs_ass_uuid_writer" : "",
    "dt_ass_uuid_executor" : "",
    "dt_ass_uuid_writer" : "",
    "enc_ass_uuid_executor" : "",
    "enc_ass_uuid_writer" : "",
    "scale_ass_uuid_executor" : "",
    "scale_ass_uuid_writer" : "",
    "ass_uuid_executor_3b" : "",
    "ass_uuid_writer_3b"   : "",
    "ass_uuid_executor_3c" : "",
    "ass_uuid_writer_3c"   : "",
    "ass_uuid_executor_3d" : "",
    "ass_uuid_writer_3d"   : ""

}
for key in uuids.keys():
    value = uuid.uuid4()
    uuids[key] = value
with open("uuids.txt","w") as f:
    for (k,v) in uuids.items():
        f.write(k+" : "+str(v)+ "\n")
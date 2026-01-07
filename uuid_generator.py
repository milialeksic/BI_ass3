import uuid
import os

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
    "ass_uuid_writer_3d"   : "", 
    "dma_ass_uuid_writer": "",
    "dma_ass_uuid_executor": "", 
    "hp_ass_uuid_writer": "", 
    "hp_ass_uuid_executor": "", 
    "split_ass_uuid_writer": "", 
    "split_ass_uuid_executor": "",
    "tafm_ass_uuid_writer": "", 
    "tafm_ass_uuid_executor": "", 
    "retrain_ass_uuid_writer": "", 
    "retrain_ass_uuid_executor": "", 
    "eval_ass_uuid": ""

}

# Function is corrected to generate uuids only for the ones that doesn't 
# already exists in uuids.txtr file. Just add the variable name in the dictionary
# and it will generate uuid for that variable, while others will be not changed
def main_function():
    UUID_FILE = "uuids.txt"
    
    # Load existing UUIDs (if file exists)
    if os.path.exists(UUID_FILE):
        with open(UUID_FILE, "r") as f:
            for line in f:
                if ":" in line:
                    key, value = line.split(":", 1)
                    key = key.strip()
                    value = value.strip()
                    if key in uuids and value:
                        uuids[key] = value
    
    # Generate UUIDs only for missing entries
    for key, value in uuids.items():
        if not value:
            uuids[key] = str(uuid.uuid4())
    
    # Write back to file
    with open(UUID_FILE, "w") as f:
        for k, v in uuids.items():
            f.write(f"{k} : {v}\n")

import sys

def just_one_uuid_generator():
    UUID_FILE = "uuids.txt"
    k = sys.argv[1]
    v = uuid.uuid4()
    if os.path.exists(UUID_FILE):
        with open(UUID_FILE, "a") as f:
            f.write(f"{k}:{v}\n")
    

if __name__=="__main__":
    just_one_uuid_generator()
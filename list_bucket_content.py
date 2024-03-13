"""
Written by Enrico Ciracì - March 2024
Create a report of the content of an S3 bucket.

Python Dependencies:
- pandas:Python Data Analysis Library
        https://pandas.pydata.org/
- boto3: The AWS SDK for Python
        https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
"""
# - Python modules
import argparse
import os
from pathlib import Path
from datetime import datetime, date
from boto3 import client
import pandas as pd

from iride_utils.aoi_info import get_aoi_info
from iride_utils.gsp_description import gsp_d_type, gsp_description

SENSOR = 'SNT'    # - Sentinel-1


def main() -> None:
    # - Argparse input argument
    parser = argparse.ArgumentParser(
        description="List the content of an S3 bucket")
    #  -  bucket name as positional argument
    parser.add_argument("bucket_name",
                        help="The name of the bucket")
    # - Optional
    # - Bucket sub-directory
    parser.add_argument("-S", "--sub_dir",
                        help="The name of the sub-directory")
    # - Output file - Absolute path
    parser.add_argument("-O", "--out_dir",
                        default=os.getcwd(),
                        help="Absolute path to output directory")
    # - Output file format
    parser.add_argument("-F", "--format",
                        default="csv", choices=["csv", "xlsx", "txt"],
                        help="The format of the output file")
    args = parser.parse_args()

    # - Initialize the connection to the S3 bucket
    conn = client('s3')  # again assumes boto.cfg setup, assume AWS S3

    # - Initialize a Pandas Dataframe containing the following columns:
    # - SVC_ID, GSP_ID, GSP_Path, Reference_Period, Delivery_Date
    gsp_df = pd.DataFrame(columns=["SVC_ID", "GSP_ID", "AOI", "GSP_Path",
                                   "Start_Date", "End_Date", "Sensor",
                                   "Data_Type", "Scheduled_Delivery_Date",
                                   "Delivery_Date", "GSP_Name"])
    # - Initialize a list of keys
    svc_id_list = []
    gsp_id_list = []
    aoi_list = []
    gsp_path_list = []
    start_date_list = []
    end_date_list = []
    s_delivery_date_list = []
    delivery_date_list = []
    sensor_list = []
    name_list = []
    d_type_list = []

    # - To skip - suffixes of filese to skip
    skip_suffixes = ["DS_Store", "qml", "sld", "/"]

    for key in conn.list_objects(Bucket=args.bucket_name)['Contents']:
        if args.sub_dir is not None and args.sub_dir in key['Key']:
            # - Extract the key
            key_name = key['Key']

            # - Extract file suffix
            file_suffix = key_name.split(".")[-1]
            if file_suffix in skip_suffixes:
                continue
            if key_name.endswith(os.sep) or key_name.endswith("/"):
                continue
            # - Split the key into a list of strings
            key_name_list = key_name.split("/")
            # - Extract the elements of the key
            svc_id = key_name_list[1]
            sensor = key_name_list[2]
            aoi_id = key_name_list[4]
            gsp_id = key_name_list[5]
            gsp_path = key_name
            # - Extract the start and end date and convert to datetime
            start_time_str = key_name_list[3].split("_")[0]
            start_date = (datetime(int(start_time_str[0:4]),
                                   int(start_time_str[4:6]),
                                   15)
                          .strftime("%d/%m/%Y"))
            end_date_str = key_name_list[3].split("_")[1]
            end_date = (datetime(int(end_date_str[0:4]),
                                 int(end_date_str[4:6]),
                                 15)
                        .strftime("%d/%m/%Y"))

            if svc_id == "SE-S3-01":
                # - Set the delivery date
                d_date = date(2024, 2, 15)
            else:
                d_date = date(2024, 3, 1)
            delivery_date = d_date.strftime("%d/%m/%Y")

            # - Append the elements to the lists
            svc_id_list.append(svc_id)
            gsp_id_list.append(gsp_id)
            gsp_path_list.append(gsp_path)
            try:
                aoi_list.append(get_aoi_info(aoi_id)['aoi_name'])
            except ValueError:
                print(f"# - Error: AOI {aoi_id} not recognized")
                import sys
                sys.exit(1)

            start_date_list.append(start_date)
            end_date_list.append(end_date)
            delivery_date_list.append(delivery_date)
            s_delivery_date_list.append("01/02/2024"
                                        if svc_id == "SE-S3-01"
                                        else "15/02/2024")
            sensor_list.append(sensor)
            d_type_list.append(gsp_d_type(gsp_id))
            name_list.append(gsp_description(gsp_id))

    # - Update the dataframe
    gsp_df["SVC_ID"] = svc_id_list
    gsp_df["GSP_ID"] = gsp_id_list
    gsp_df["GSP_Path"] = gsp_path_list
    gsp_df["AOI"] = aoi_list
    gsp_df["Start_Date"] = start_date_list
    gsp_df["End_Date"] = end_date_list
    gsp_df["Delivery_Date"] = delivery_date_list
    gsp_df["Scheduled_Delivery_Date"] = s_delivery_date_list
    gsp_df["Sensor"] = sensor_list
    gsp_df["Data_Type"] = d_type_list
    gsp_df["GSP_Name"] = name_list

    # - Save the produced dataframe to a file
    out_path \
        = Path(args.out_dir) / Path(f"Lot-2_GSP_Delivery_Report-"
                                    f"{datetime.now().strftime('%Y%m%d')}"
                                    f".{args.format}")
    if args.format == "csv":
        gsp_df.to_csv(out_path, index=False)
    elif args.format == "xlsx":
        gsp_df.to_excel(out_path, index=False, header=True,
                        sheet_name="GSP-Delivery")
    elif args.format == "txt":
        gsp_df.to_csv(out_path, index=False, sep="\t")
    else:
        print("# - Error: Format not recognized")


if __name__ == "__main__":
    start_time = datetime.now()
    main()
    end_time = datetime.now()
    print(f"# - Computation Time: {end_time - start_time}")

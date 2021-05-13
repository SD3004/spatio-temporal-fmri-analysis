DBHOST=https://db.humanconnectome.org
PROJECT=HCP_1200
REST_URL_PREFIX=$DBHOST/data/archive/projects/$PROJECT/subjects
##################################################################################################################
#
# GET a jsession
#
#
# Set
#
# MY_CURL_OPTIONS: Options that you may want to pass to curl such as --connect-timeout, --retry etc
# db_user: ConnectomeDB login id
# db_password: ConnectomeDB password
#
#
# subject_list_file: A File containing list of subject IDs
#
##################################################################################################################

jsession='curl $MY_CURL_OPTIONS -u ${username}:$db_password ${pwd}'
 
while read line
do
    subject=$line
    subject_url_prefix=$REST_URL_PREFIX/$subject/experiments/${subject}_CREST/resources/${subject}_CREST/files
    #file_relative_path=MNINonLinear/Results/rfMRI_REST1_LR/rfMRI_REST1_LR_Atlas_MSMAll.dtseries.nii
    #file_relative_path=MNINonLinear/Results/rfMRI_REST2_LR/rfMRI_REST2_LR_Atlas_MSMAll.dtseries.nii
    file_relative_path=MNINonLinear/Results/rfMRI_REST1_LR/rfMRI_REST1_LR_Atlas_hp2000_clean.dtseries.nii
    echo $subject_url_prefix/$file_relative_path 
    #curl -u sd3004:11@Raphaella30 -o /data/HCP/rfMRI/rfMRI_REST1_LR/${subject}_rfMRI_REST1_LR_Atlas_MSMAll.dtseries.nii --create-dir $subject_url_prefix/$file_relative_path
    #curl -u sd3004:11@Raphaella30 -o /data/HCP/rfMRI/rfMRI_REST2_LR/${subject}_rfMRI_REST1_LR_Atlas_MSMAll.dtseries.nii --create-dir $subject_url_prefix/$file_relative_path
    curl -u sd3004:11@Raphaella30 -o /data/HCP/rfMRI/test/${subject}_rfMRI_REST1_LR_Atlas_hp2000_clean.dtseries.nii --create-dir $subject_url_prefix/$file_relative_path
done <HCP_subject.csv
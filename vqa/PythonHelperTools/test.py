from shutil import copyfile
from vqaTools.vqa import VQA
import random
import skimage.io as io
import matplotlib.pyplot as plt
import os
import argparse
import json

def main(params):
	dataDir=params['dataDir']
	vqaDir=params['vqaDir']
	taskType='OpenEnded'
	dataType='mscoco' # 'mscoco' for real and 'abstract_v002' for abstract
	dataSubType='train2014'
	annFile='%s/Annotations/%s_%s_annotations.json'%(dataDir, dataType, dataSubType)
	quesFile='%s/Questions/%s_%s_%s_questions.json'%(dataDir, taskType, dataType, dataSubType)
	imgDir = '%s/Images/%s/%s/' %(dataDir, dataType, dataSubType)
	dataDir=params['dataDir']+"/"
	vqaDir=params['vqaDir']+"/"
	 
	vqa=VQA(annFile, quesFile)
	data=[]
	annIds = list(set(vqa.getImgIds()))[:params['num']]
	for id in annIds:
		imgFilename = 'mscoco/train2014/COCO_' + dataSubType + '_'+ str(id).zfill(12) + '.jpg'
		copyfile(dataDir+imgFilename, vqaDir+imgFilename)
		caption=[]
		caption2=[]
		for i in vqa.imgToQA[id]:
			caption.append(vqa.qqa[i['question_id']]['question'])
			caption.append(vqa.qqap[i]['question_id']['choices'])
		data.append({"file_path":imgFilename,"captions":caption})


	with open('data.json','w') as outfile:
	 	json.dump(data,outfile)

parser = argparse.ArgumentParser()
parser.add_argument('--num', default=16, type=int, help='Enter --num parameter: Number of images to create for')
parser.add_argument('--dataDir',default='..', help='The base directory for the data and other stuff')
parser.add_argument('--vqaDir',default='..', help='The base directory for the data and other stuff')

args = parser.parse_args()
params = vars(args) # convert to ordinary dict
main(params)

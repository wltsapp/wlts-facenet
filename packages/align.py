from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import sys
from packages import preprocess

input_datadir= './train_img'
output_datadir = './pre_img'

print ("Align Start")
obj=preprocess.preprocesses(input_datadir,output_datadir)
get_file=obj.collect_data()
print('Aligned classifier model to file "%s"' % get_file)
sys.exit("All Done")

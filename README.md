# Multi-Category-Graph-Image-Classification

## Complete Code
- Open “CE_Assgnment.ipynb” file for the complete code.
## Model File
- File with name “epoch10.pt”.
## Model Accuracy Report 
- File with name “MAR.docx”.

### Data Set Used:
vis10cat.txt : 2223 URLs in 10 categories <br> A tab-delimited file with each line giving the category and then the URL of an image.

Note: The data given in vis10cat.txt after downloading and removing corrupted file was only 759 as many links were not working and some files were corrupted.<br>
Hence after the training the model on that dataset, model was over fitting.<br>
That data is in “https://bit.ly/3AF8EKg”.<br>
So, in order to train our model in a better way I scraped some data from Google Images one by one using the code given in the file “graphextr.py”.<br>
That data is in “https://bit.ly/2XMa9bB”.<br>

Master folder containing both the data mixed is “https://bit.ly/3EwuKkN” having 2864 images to be exact.<br><br>

To run the file,
1.	Upload the Jupyter Notebook to your Google Collab.
2.	Mount your google drive from “Mounting Google drive” section in the notebook.
3.	Place the “epoch10.pt" (https://bit.ly/3lCC5GA) file in path "/content/drive/MyDrive/encoder/epoch10.pt".
4.	Place the test image in path "/content/test.jpg" having name test.jpg
5.	Go to the “Run pretrained model From Here” section of the code and run it.

The code for training the model is from starting of the notebook up to the section named “Model”.<br>
The validation accuracy of the model can also be seen the “Model” section.<br>
If training the model again,<br>
Put the “https://bit.ly/3EwuKkN” folder at the path "/content/drive/MyDrive/Plot_Data/" and run the whole code up to the “Model” section.<br>

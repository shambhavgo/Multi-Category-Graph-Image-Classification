# Multi-Category-Graph-Image-Classification

 	Complete Code
- Open “CE_Assgnment.ipynb” file for the complete code.
 	Model File
- File with name “epoch10.pt”.
 	Model Accuracy Report 
- File with name “MAR.docx”.

Note: The data given in vis10cat.txt after downloading and removing corrupted file was only 759 as many links were not working and some files were corrupted.
Hence after the training the model on that dataset, model was over fitting.
That data is in a folder named “vis10cat Data”.
So, in order to train our model in a better way I scraped some data from Google Images one by one using the code given in the file “graphextr.py”.
That data is in a folder named “Scraped Data”.

Master folder containing both the data mixed is named “Plot_Data” having 2864 images to be exact.

To run the file,
1.	Upload the Jupyter Notebook to your Google Collab.
2.	Mount your google drive from “Mounting Google drive” section in the notebook.
3.	Place the “epoch10.pt” file in path "/content/drive/MyDrive/encoder/epoch10.pt".
4.	Place the test image in path "/content/test.jpg" having name test.jpg
5.	Go to the “Run pretrained model From Here” section of the code and run it.

The code for training the model is from starting of the notebook up to the section named “Model”.
The validation accuracy of the model can also be seen the “Model” section.
If training the model again,
Put the “Plot_Data” folder at the path "/content/drive/MyDrive/Plot_Data/" and run the whole code up to the “Model” section.
The answers to MCQ and Open-ended questions are in MCQ.docx & OEQ.docx.

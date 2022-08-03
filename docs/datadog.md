# **Datadog**

## **Authentication for datadog**
- Name - what is this used for? : Auth for Datadog
- url : https://app.datadoghq.com
- click on submit button 

## **Webhook**
Webhooks enable you to:

- Connect to your services.
- Alert your services when a metric alert is triggered
### Follow below given step to create webhook 
- Go to [shuffle](https://shuffler.io/)
- click on the workflow and in workflow you click on triggers **(at bottom of the left corner)**
- Drag and drop webhooks **(custom HTTP input)**
  ![image](https://user-images.githubusercontent.com/60142831/181471655-f2c0f042-0cf1-48dd-a8e0-488eac27efad.png)

- At the right side one button is there in patameters **(start)** Click on start button and copy that URL
  ![image](https://user-images.githubusercontent.com/60142831/181472812-f6d907f9-2fde-4af3-a077-c0ff526525c3.png)

- You'll need to go to the [datadog](https://app.datadoghq.com/account/login?next=%2F%3F_gl%3D1%2A1myfg5d%2A_ga%2AMTE2OTg3NTUwNC4xNjU3NjA1MTk0%2A_ga_KN80RDFSQK%2AMTY1ODk4NzY2MS4yMy4xLjE2NTg5ODg0NDkuNjA.%26_ga%3D2.247342660.1562540511.1658898756-1169875504.1657605194e)
- login with your datadog account
- click on integration panel at the left side now search webhook in the integration
- click on webhook
 ![image](https://user-images.githubusercontent.com/60142831/181470285-efde130e-3cc3-4a8f-93d2-3280fd93ae9e.png)

- Scroll down the popup menu and find the webhook title 
And click new button
![image](https://user-images.githubusercontent.com/60142831/181473479-e3ba367e-2c54-4b5b-875b-57a31c906390.png)
- put name and url for new webhook
  
  ![image](https://user-images.githubusercontent.com/60142831/181474508-bc924783-9123-4893-8200-9ab86a5927a8.png)
  - name : datadog-webhook
  - URL :  copied url (paste here)

### Create Metric

### Follow below given step to create Metric 
- You'll need to go to the [datadog](https://app.datadoghq.com/account/login?next=%2F%3F_gl%3D1%2A1myfg5d%2A_ga%2AMTE2OTg3NTUwNC4xNjU3NjA1MTk0%2A_ga_KN80RDFSQK%2AMTY1ODk4NzY2MS4yMy4xLjE2NTg5ODg0NDkuNjA.%26_ga%3D2.247342660.1562540511.1658898756-1169875504.1657605194e)
- click on monitor in that you select the new Monitor
- Click New Monitor in the upper right of the screen. Under “Select a monitor type” click Metric.
  
  ![image](https://user-images.githubusercontent.com/60142831/181475534-23ba4d3d-f650-4b69-934c-d5e32a21c60b.png)

- **5 steps are given in this screen**
  
  1. Choose the detection method
       - select the threshold Alert tab
![image](https://user-images.githubusercontent.com/60142831/181476549-eb78b57f-b6ab-4196-a59b-188c03580990.png)
  2. Define the metric
       - select edit tab and type in below system.cpu.idle
![image](https://user-images.githubusercontent.com/60142831/181476583-bb4cea32-ba97-44da-b03f-378fdbf92d09.png)
  3. Set alert conditions
       - set Trigger when the metric is **below or equal to** the threshold **at least once** during the last **5 minutes**
       - set Alert threshold is **100**
       - set **notify** if data is missing for more than **8** minutes.
![image](https://user-images.githubusercontent.com/60142831/181476583-bb4cea32-ba97-44da-b03f-378fdbf92d09.png)
  4. Notify your team
       -  click on edit and put **Example Monitor Name** : CPU is extremely high{{host.name}}
       -  select webhook name in given dropdown menu
![image](https://user-images.githubusercontent.com/60142831/181476647-63fec8a9-76b9-4e75-9ae6-f0d8e6a8918f.png)
  1. Define permissions and audit notification
        - click the save
        ![image](https://user-images.githubusercontent.com/60142831/181476664-5779c7c0-3e91-4b55-8d0e-e09d87e70666.png)
   



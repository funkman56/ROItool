'''
ROI(region of interest)
手動圈選區域追蹤
'''

import cv2

print("\n~~~請選擇你要追蹤物件的方法~~~")
method = {"1": "CSRT","2":"KCF","3":"TLD","4":"MIL","5":"MOSSE","6":"Boosting","7":"MedianFlow"}

number = input("1. CSRT       2. KCF\n3. TLD        4. MIL\n5. MOSSE      6. Boosting\n7. MedianFlow\n>>  ")


try :
    print("\n追蹤算法 :",method[number])
    name = input("影片名稱 : ")
    filetype = input("影片格式 : ")
    
    '''
    if elif else 單行寫法
    True1 if Condition1 else True2 if Condition2 else True3 ... if Condition#n-1 else True#n  
    '''
    tracker = cv2.TrackerCSRT_create() if int(number) == 1 else cv2.TrackerKCF_create() if int(number) == 2 else cv2.TrackerTLD_create() if int(number) == 3 else cv2.TrackerMIL_create() if int(number) == 4 else cv2.TrackerMOSSE_create() if int(number) == 5 else cv2.TrackerBoosting_create() if int(number) == 6 else cv2.TrackerMedianFlow_create()  
    
    #print(type(tracker))
    #tracker = cv2.TrackerCSRT_create()
    #tracker = cv2.TrackerKCF_create()
    #tracker = cv2.TrackerTLD_create()
    #tracker = cv2.TrackerMIL_create()
    #tracker = cv2.TrackerMOSSE_create()
    #tracker = cv2.TrackerBoosting_create()
    #tracker = cv2.TrackerMedianFlow_create()
    
    try :
        cap = cv2.VideoCapture('C:/Users/Relieak/Desktop/{}.{}'.format(name,filetype))
        
        initTarget = None
        
        while True:
            
            ret, frame = cap.read()
            
            if initTarget is None:
                
                initTarget = cv2.selectROI('video', frame)   
                tracker.init(frame, initTarget)
                
                
            else:
                
                success, rect = tracker.update(frame)
                
                if success:
                    
                    (x, y, w, h) = [int(i) for i in rect]                                # 視窗最左上角(x,y)=(0,0)，長度單位是Pixel，1px = 0.04cm
                    #print((x, y, w, h))
                    
                  # cv2.rectangle(影像, 頂點座標, 對向頂點座標, 顏色, 線條寬度)            
                    cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2) 
            
            try :
        
                cv2.imshow('video', frame)                                              # error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'cv::imshow'
            
            except :
                
                print("\n物件追蹤失敗，視窗已經關閉 !")
                cv2.destroyAllWindows()
                break
            
             # cv2.waitKey(X)，等待 X ms毫秒,在此期間如果有鍵按下則立即結束並返回按下的那個按鍵的ASCII碼
              
            if cv2.waitKey(66) == 27 :                                                   # 27 是對應鍵盤的 ESC (ASCII碼)
                
                cv2.destroyAllWindows()
                break
            
    except :
            
        print("\n無此影片名稱或格式錯誤 !!!")
        
        
except :
    
    print("\n輸入錯誤 !")
    cv2.destroyAllWindows()
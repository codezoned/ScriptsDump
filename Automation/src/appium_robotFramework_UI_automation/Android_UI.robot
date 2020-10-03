*** Keywords ***

Open the App
    Open Application    ${APPIUM_SERVER}  platformName=${PLATFORM_NAME}  platformVersion=${PLATFORM_VERSION}  deviceName=${DEVICE_NAME}
    ...                 automationName=${AUTOMATOR_NAME}  app=${APP}  appPackage=${PACKAGE_NAME}  appActivity=${ACTIVITY_NAME}  
Open the Real App
    Open Application    ${APPIUM_SERVER}  platformName=${PLATFORM_NAME}  platformVersion=${PLATFORM_VERSION}  deviceName=${DEVICE_NAME}
    ...                 automationName=${AUTOMATOR_NAME}  appPackage=${PACKAGE_NAME}  appActivity=${ACTIVITY_NAME}


Move to main screen
    Click Element    id=${allow_button}
    Sleep  2s
    Click Element    id=${allow_button}
    Sleep  5s

Choose Single Mode
    Click Element    accessibility_id=Single Instance
    Sleep  5s
    Input Text    id=com.android.fun:id/key  title,eventName
    Input Text    id=com.android.fun:id/value  test1,test2
    Click Element    id=com.android.fun:id/done
    Sleep  2s

Choose Video
    Click Element    xpath=/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[2]

ExoAndroid Specific Navigation
    Move to main screen
    Choose Single Mode
    Choose Video

Pause and Resume the Video
    TAP  com.android.akamai.sampleexoplayer:id/exo_overlay  count=1
    Click Element    accessibility_id=Pause
    Sleep  5s
    Click Element    accessibility_id=Play

Press Forward and Backward
    TAP  com.android.akamai.sampleexoplayer:id/exo_overlay  count=1
    Click Element    accessibility_id=Fast-forward
    Sleep  5s
    TAP  com.android.akamai.sampleexoplayer:id/exo_overlay  count=1
    Click Element    accessibility_id=Rewind

Press Back Button 
    Press Keycode  4

Press Home Button
    Press Keycode  3

Store the Logs
    Get Device Plugin Logs
    
Start App
    Launch Application
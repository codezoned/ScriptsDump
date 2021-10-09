// CodeForces - Contest Notifier: This tool first logs in to your CodeForces id and then registers to all the contests available at the moment for you.
// It also scrapes the already registered and upcoming contests' data and notifies you of the dates and time of all contests through a text via Whatsapp Web.
// Tech-Stacks : JavaScript, HTML, CSS, puppeteer

const pup = require("puppeteer");
let fs = require('fs');
let email = ""; //type in your email and password to use automatic contest notifier
let password = "";
let url = "https://codeforces.com/";
async function main(){
    let browser = await pup.launch({ // opens the browser
        headless: false,
        defaultViewport: false,
        args: ["--start-maximized"]// fullscreen
    });
    let pages = await browser.pages();// browser ke andar opened tabs ko ek array mien leke aana
    tab = pages[0];
    await tab.goto(url);
    await tab.waitForSelector(".menu-list.main-menu-list",{visible:true});// wait for a css selector to load on page
    let list = await tab.$$(".menu-list.main-menu-list li a");
    let contest = list[2];
    let contestUrl = await tab.evaluate(function(ele){
        return ele.getAttribute("href");
    },contest);
    await tab.goto("https://codeforces.com"+contestUrl);// goes to codeforces main site
    await tab.waitForSelector(".lang-chooser",{visible:true,setTimeout:2000});
    let enterRegister = await tab.$$(".lang-chooser a");
    let enter = enterRegister[2];
    let enterHref = await tab.evaluate(function(ele){
        return ele.getAttribute("href"); // gets hyperlink address
    },enter);
    await tab.goto("https://codeforces.com"+enterHref);
    await tab.waitForSelector("#handleOrEmail",{visible:true,setTimeout:2000});
    await tab.type("#handleOrEmail",email); // types in email password asynchronusly
    await tab.type("#password",password);
    await tab.click("input[value='Login']");
    await tab.waitForSelector("div[style='background-color: white;margin:0.3em 3px 0 3px;position:relative;']",{visible:true,setTimeout:2000});
    let tables = await tab.$$("div[style='background-color: white;margin:0.3em 3px 0 3px;position:relative;'] table");
    //console.log(tables.length);
    let rows = await tables[0].$$("tr");
    //console.log(rows.length);
    let remindDates = [];
    let registerUrls = [];
    for(let i=1;i<rows.length;i++){
        let columns = await rows[i].$$("td");
        let aTagCount = await columns[columns.length-1].$$("a");
        if(aTagCount.length==2){
            let hrefCalc = await tab.evaluate(function(ele){
                return ele.getAttribute("href");
            },aTagCount[0]);
            registerUrls.push("https://codeforces.com"+hrefCalc);
        }
        else{
            //creating data of contests and their timings
            let data = {};
            let text = await columns[columns.length-2].$(".countdown");
            let innerText = await tab.evaluate(function(ele){
                return ele.textContent;
            },text);
            let nameOfContest = await tab.evaluate(function(ele){
                return ele.textContent;
            },columns[0]);
            let timeValue = await columns[2].$("a");
            let time =await tab.evaluate(function(ele){
                return ele.textContent;
            },timeValue)
            data["Name"]=nameOfContest;
            let today = new Date();
            let day = parseInt(today.getDate());
            let month = parseInt(today.getMonth());
            month++;
            if(month<10){
                month="0"+month;
            }
            //extracting date time etc. from the contest timeline
            if(innerText.includes("days")|| innerText.includes("day")){
               let numberOfDaysToAdd = parseInt(innerText.split(" ")[0]) ; 
               //console.log(numberOfDaysToAdd);
               //console.log(day +" "+ month);
               let finalDay = parseInt(day+numberOfDaysToAdd);
               if(month == "02"){
                   if(finalDay>28){
                     finalDay = finalDay - 28;
                     month = parseInt("03");
                   }
               }
               else if(month =="04"||month=="06"||month=="09"||month=="11"){
                   if(finalDay>30){
                       finalDay = finalDay-30;
                       month = parseInt(month)+1;
                   }
               }
               else{
                   if(finalDay>31){
                       finalDay = finalDay - 31;
                       month = parseInt(month)+1;
                   }
               }
               let dateOfContest = `${finalDay} ${month} 2021`;
               data["Date"]=dateOfContest;
               data["Time"] =time;
            }
            else{
                data["Date"] = `${day} ${month} 2021`;
                data["Time"] = time;
            }
            remindDates.push(data);
        }
    }
    fs.writeFileSync("contests.json",JSON.stringify(remindDates));
    for(let i in registerUrls){
        await tab.goto(registerUrls[i]);
        await tab.waitForSelector("input[value='Register']",{visible:true});
        await tab.click("input[value='Register']");
        await tab.waitForSelector(".welldone");
    }
    setTimeout(()=>{

    },2000);
    //goes to whatsapp web to send in notification
    await tab.goto("https://web.whatsapp.com/");
    await tab.waitForSelector("._13NKt.copyable-text.selectable-text",{visible:true});
    await tab.type("._13NKt.copyable-text.selectable-text","Tattu Bear"); // type in contact name to send in the whatsapp msg
    await tab.keyboard.press("Enter"); // keypress
    await tab.waitForSelector("div[tabindex='-1']",{visible:true,setTimeout:3000});
    let readData = fs.readFileSync("contests.json","utf-8");
    let lines = readData.split(",");
    //reading the data file to type in contest details
    for(let j in lines){
        let ans = "";
        let chars = lines[j];
       if(chars!=""){
        for(let k in chars){
            if(chars[k]!="[" && chars[k]!= "{" && chars[k] && chars[k]!="}" && chars[k]!=']'){
                ans+= chars[k];
            }
        }
       }
        console.log(ans);
        await tab.waitForSelector("._13NKt.copyable-text.selectable-text",{visible:true,setTimeout:2000});
        console.log(1);
        // let sel2 = await tab.$$("._13NKt.copyable-text.selectable-text");
        await tab.type(".p3_M1",ans);
        await tab.keyboard.press("Enter");
    }
}

main();
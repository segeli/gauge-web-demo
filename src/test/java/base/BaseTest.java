package base;


import java.net.URL;
import java.util.concurrent.TimeUnit;

import org.apache.commons.lang3.StringUtils;
import org.openqa.selenium.Platform;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.ie.InternetExplorerDriver;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;

public class BaseTest {

    protected WebDriver driver;
    public String baseUrl = "https://www.modanisa.com/";

    public void setUp() throws Exception {
    	System.out.println("setUp invoked..");
    	DesiredCapabilities capabilities = DesiredCapabilities.chrome();
    	capabilities.setPlatform(Platform.LINUX);
		String key = System.getProperty("key");
		
		/*
        String PROXY = "ec2-54-154-66-64.eu-west-1.compute.amazonaws.com:3128"; 
        Proxy proxy = new org.openqa.selenium.Proxy();
		proxy.setProxyType(ProxyType.MANUAL);
		proxy.setHttpProxy(PROXY);
		proxy.setFtpProxy(PROXY);
		proxy.setSslProxy(PROXY);
		proxy.setSocksProxy(PROXY);
		dc.setCapability(CapabilityType.PROXY, proxy);*/
		
		ChromeOptions co = new ChromeOptions();
        co.addArguments("--start-maximized");
        co.addArguments("--start-fullscreen");
		
        baseUrl = "http://dev.testinium.com/";
        System.out.println("KEY: " + key);
		if(StringUtils.isNotEmpty(key)){
			System.out.println("key:" + key);
			capabilities.setCapability("key", key);
			capabilities.setCapability(InternetExplorerDriver.IE_SWITCHES, "");
			driver = new RemoteWebDriver(new URL("http://192.168.60.161:4444/wd/hub"),capabilities);
		} else {
			System.setProperty("webdriver.chrome.driver", "src/test/resources/chromedriver.exe");
			capabilities.setCapability(ChromeOptions.CAPABILITY, co);
	        driver = new ChromeDriver(capabilities);
		}
    	
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
    }

    public void tearDown() throws Exception {
    	driver.quit();
    }

}

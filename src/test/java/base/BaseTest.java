package base;


import com.thoughtworks.gauge.AfterScenario;
import com.thoughtworks.gauge.AfterSpec;
import com.thoughtworks.gauge.BeforeScenario;
import com.thoughtworks.gauge.BeforeSpec;
import org.apache.commons.lang3.StringUtils;
import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.openqa.selenium.Platform;
import org.openqa.selenium.Proxy;
import org.openqa.selenium.Proxy.ProxyType;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.ie.InternetExplorerDriver;
import org.openqa.selenium.remote.CapabilityType;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;

import java.net.URL;
import java.util.concurrent.TimeUnit;

public class BaseTest {

    protected static WebDriver driver;
    public String baseUrl = "https://www.modanisa.com/";

    @BeforeScenario
    public void setUp() throws Exception {
    	DesiredCapabilities capabilities = DesiredCapabilities.chrome();
    	capabilities.setPlatform(Platform.LINUX);
		String key = System.getProperty("key");
		
		ChromeOptions co = new ChromeOptions();
        co.addArguments("--start-maximized");
        co.addArguments("--start-fullscreen");
		
		if(StringUtils.isNotEmpty(key)){
			capabilities.setCapability("key", key);
			capabilities.setCapability(InternetExplorerDriver.IE_SWITCHES, "");
			driver = new RemoteWebDriver(new URL("http://localhost:4444/wd/hub"),capabilities);
		} else {
			System.setProperty("webdriver.chrome.driver", "src/test/resources/chromedriver.exe");
			capabilities.setCapability(ChromeOptions.CAPABILITY, co);
	        driver = new ChromeDriver(capabilities);
		}
    	
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
    }

    @AfterScenario
    public void tearDown() throws Exception {
    	driver.quit();
    }

}

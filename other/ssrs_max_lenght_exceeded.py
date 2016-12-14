There was an exception running the extensions specified in the config file. ---> Maximum request length exceeded. ---> 

Solution:
 1) goto D:\Microsoft SQL Server\MSRS10.MSSQLSERVER\Reporting Services\ReportServer (in case its SG14 server)
 2) change in web.config file:
     from 
     <httpRuntime executionTimeout=”9000″ />
     to
     <httpRuntime executionTimeout=”9000″ maxRequestLength = “16384” />
 3) maybe ssrs restart will be needed
     

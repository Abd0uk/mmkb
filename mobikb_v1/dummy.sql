INSERT INTO providers_countrydata VALUES(1,'EG','not required',1);
INSERT INTO providers_countrydata VALUES(2,'DZ','not required',1);
INSERT INTO providers_countrydata VALUES(3,'GB','not required',1);
INSERT INTO providers_countrydata VALUES(4,'CN','not required',2);
INSERT INTO providers_countrydata VALUES(5,'HK','Required',2);
INSERT INTO providers_countrydata VALUES(6,'TW','Required',2);
INSERT INTO providers_network VALUES(1,'Orange');
INSERT INTO providers_network VALUES(2,'Ooredoo');
INSERT INTO providers_network VALUES(3,'H3G');
INSERT INTO providers_network VALUES(6,'O2');
INSERT INTO providers_network VALUES(7,'Vodafone');
INSERT INTO providers_network VALUES(8,'China Telecom');
INSERT INTO providers_network VALUES(9,'Chunghwa');
INSERT INTO providers_countrydata_networks VALUES(1,2,2);
INSERT INTO providers_countrydata_networks VALUES(2,1,1);
INSERT INTO providers_countrydata_networks VALUES(3,3,3);
INSERT INTO providers_countrydata_networks VALUES(4,3,6);
INSERT INTO providers_countrydata_networks VALUES(5,3,7);
INSERT INTO providers_countrydata_networks VALUES(6,4,8);
INSERT INTO providers_countrydata_networks VALUES(7,5,8);
INSERT INTO providers_countrydata_networks VALUES(8,6,9);
INSERT INTO providers_operator VALUES(1,'Airalo','Airalo','Check Admin Panel','Same','App / Website','n/a','https://mobimatter.com/topup-esim/Airalo/all','Validity will start upon downloading the eSIM & Connects to a network','Delete & Redownload - max 5 times.','Refund is possible if not activated- ask the operator. If activated with little to no usage- can check if the operator agrees.','Check by Scan','n/a');
INSERT INTO providers_operator VALUES(2,'3HK','3','mobile.three.com.hk','same+1','website / app','n/a','https://mobimatter.com/topup-esim/3/all','n/a','n/a','n/a','Yes','n/a');
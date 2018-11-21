# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 15:17:40 2018

@author: Ruslan
"""

from linkedin import linkedin
import config 

authentication = linkedin.LinkedInDeveloperAuthentication(
                    config.CONSUMER_KEY,
                    config.CONSUMER_SECRET,
                    config.USER_TOKEN,
                    config.USER_SECRET,
                    config.RETURN_URL,
                    linkedin.PERMISSIONS.enums.values()
                )



application = linkedin.LinkedInApplication(authentication)


profile = application.search_company(selectors=[{'companies': ['id','name', 'universal-name', 'website-url']}], params={'keywords': 'cotrader'})

print(profile)
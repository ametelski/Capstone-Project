import {HttpModule} from '@angular/http';
import {RouterModule} from '@angular/router';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';

import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { SignUpComponent } from './sign-up/sign-up.component';
import { appRoutes } from '../routes';
import { WelcomeComponent } from './welcome/welcome.component';
import { TempRestService } from './temp-rest.service';
import { SkillpathService } from './skillpath.service';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    SignUpComponent,
    WelcomeComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(appRoutes),
    HttpModule
  ],
  providers: [
    TempRestService,
    SkillpathService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
import {Routes} from '@angular/router';
import { SignUpComponent } from './app/sign-up/sign-up.component';
import { WelcomeComponent } from './app/welcome/welcome.component';
import { LoginComponent } from './app/login/login.component';


export const appRoutes: Routes = [
  {path: 'sign-up', component: SignUpComponent},
  {path: '', redirectTo: '/home', pathMatch: 'full'},
  {path: 'welcome', component: WelcomeComponent},
  {path: 'login', component: LoginComponent}
]

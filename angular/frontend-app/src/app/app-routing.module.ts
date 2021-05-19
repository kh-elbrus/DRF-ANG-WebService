import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AddnewarticleComponent } from './addnewarticle/addnewarticle.component';
import { AddnewcategoryComponent } from './addnewcategory/addnewcategory.component';
import { AppComponent } from './app.component';
import { ArticlesideComponent } from './articleside/articleside.component';
import { HomesideComponent } from './homeside/homeside.component';
import { LoginsideComponent } from './loginside/loginside.component';
import { ProfileComponent } from './profile/profile.component';
import { RegistrationsideComponent } from './registrationside/registrationside.component';
import { AuthGuardService } from './auth-guard.service';

const routes: Routes = [
  {path: '', component: AppComponent, canActivate: [ AuthGuardService ]},
  {path: 'login', component: LoginsideComponent},
  {path: 'registration', component: RegistrationsideComponent},
  {path: 'home', component: HomesideComponent},
  {path: 'profile', component: ProfileComponent, canActivate: [ AuthGuardService ]},
  {path: 'articles', component: ArticlesideComponent, canActivate: [ AuthGuardService ]},
  {path: 'new-article', component: AddnewarticleComponent, canActivate: [ AuthGuardService ]},
  {path: 'new-category', component: AddnewcategoryComponent, canActivate: [ AuthGuardService ]},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

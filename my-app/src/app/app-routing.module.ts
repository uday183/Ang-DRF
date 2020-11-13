import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginpageComponent } from './loginpage/loginpage.component';
import { ProductComponent } from './product/product.component';
import { RegisterComponent } from './register/register.component';
import { ForgotpasswordComponent } from './forgotpassword/forgotpassword.component';
import { NewsComponent } from './news/news.component';
import { FriendslistComponent } from './friendslist/friendslist.component';
import { MyaccountComponent } from './myaccount/myaccount.component';
const routes: Routes = [
  {
    path: '',
    component: LoginpageComponent,
  },
  {
    path : 'products',
    component : ProductComponent
  },
  {
    path : 'register',
    component : RegisterComponent
  },
  {
    path : 'forgotpassword',
    component : ForgotpasswordComponent
  },
  {
    path : 'news',
    component : NewsComponent
  },
  {
    path : 'friendslist',
    component : FriendslistComponent
  },
  {
    path : 'myaccount',
    component : MyaccountComponent
  },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

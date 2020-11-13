import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-loginpage',
  templateUrl: './loginpage.component.html',
  styleUrls: ['./loginpage.component.css']
})
export class LoginpageComponent implements OnInit {

  isSomethingWrong = false;
  message = '';

  constructor(
    private router: Router,
    private apiService: ApiService
    ) { }

  loginForm = {
    username: '',
    password: ''
  };
  ngOnInit(): void {
  }


  login(): void{
    // console.log(this.loginForm);
    this.apiService.LoginInfo(this.loginForm).subscribe((result: any) => {
      console.log('login data ===>', result);
      sessionStorage.setItem('user_id', result.data.user_id);
      sessionStorage.setItem('username', result.data.user_name);
      if (result.status === false){
        this.isSomethingWrong = true;
        setTimeout(() => {
          this.isSomethingWrong = false;
     }, 3000);
        this.message = result.msg;
        console.log(this.message);
        this.router.navigate(['/']);

      }
      else{
        this.isSomethingWrong = false;
        this.message = '';
        this.router.navigate(['/news']);
      }
     });

  }

}

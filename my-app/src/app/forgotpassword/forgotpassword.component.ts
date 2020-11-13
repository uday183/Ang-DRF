import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { Router } from '@angular/router';
@Component({
  selector: 'app-forgotpassword',
  templateUrl: './forgotpassword.component.html',
  styleUrls: ['./forgotpassword.component.css']
})
export class ForgotpasswordComponent implements OnInit {

  constructor(
    private router: Router,
    private apiService: ApiService) { }


  forgotPasswordForm = {
    username: '',
    email: '',
    password1: '',
    password2: ''
  };

  ngOnInit(): void {
  }

  forgotpassword(): void{
    console.log('forgot password page is calling...');
    this.apiService.ForgotPassword(this.forgotPasswordForm).subscribe((result: any) => {
      console.log('Result ===>', result);
      this.router.navigate(['/']);
      });
  }
}

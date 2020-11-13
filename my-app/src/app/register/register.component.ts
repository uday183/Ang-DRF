import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from '../api.service';
@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  constructor(
    private router: Router,
    private apiService: ApiService
  ) {}
  registerForm = {
    username: '',
    email: '',
    password: ''
  };
  ngOnInit(): void {
  }

  register(): void{
      console.log('calling register page..');
      this.apiService.Register(this.registerForm).subscribe((result: any) => {
        // console.log('Result ===>', result);
          this.router.navigate(['/']);
       });
  }

}

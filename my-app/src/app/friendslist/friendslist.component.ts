import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-friendslist',
  templateUrl: './friendslist.component.html',
  styleUrls: ['./friendslist.component.css']
})
export class FriendslistComponent implements OnInit {

  constructor(
    private router: Router,
    private apiService: ApiService
  ) { }
  friends = [];
  userid;
  ngOnInit(): void {
    this.getfriends();
  }

  getfriends(): void{
    this.userid = sessionStorage.getItem('user_id');
    this.apiService.GetFriends(this.userid).subscribe((result: any) => {
      this.friends = result.data;
      console.log('get--friends ===>', this.friends);
     });
  }

}

import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-news',
  templateUrl: './news.component.html',
  styleUrls: ['./news.component.css']
})
export class NewsComponent implements OnInit {

  constructor(
    private router: Router,
    private apiService: ApiService,
    private formBuilder: FormBuilder,
  ) { }


  userid ;
  posts ;
  postid ;
  getcomments;
  divID;
  isComment = false;
  likedcount ;
  LikeddivID;
  userslist;
  acceptlist;
  acceptlistFlag = false;
  sharefriends = [];
  userdata = [];
  myFiles: string[] = [];
  usertext = '';
  uploadForm: FormGroup;
  ngOnInit(): void {
    this.userPost();
    this.friendAccept();
    this.shareFriends();
    this.userInformation();
    this.uploadForm = this.formBuilder.group({profile: ['']});
  }

  userPost(): void{
    this.userid = sessionStorage.getItem('user_id');
    this.apiService.UserPost(this.userid).subscribe((result: any) => {
      this.posts = result.data;
      console.log('UserPost ===>', result);
     });
  }

  divopen(id): void{
    this.isComment = !this.isComment;
    this.divID = id;
    this.apiService.GetComment(id).subscribe((result: any) => {
      this.getcomments = result.data;
      console.log('get--comments ===>', result);
     });
  }

  usrcomment(usercomment, postid): void{
    // alert(usercomment.comment_id);
    this.apiService.UserComment(postid, this.userid, usercomment ).subscribe((result: any) => {
      this.getcomments = result.data;
      console.log('get--comments ===>', result);
     });
  }

  userliked(postid): void{
    this.LikeddivID = postid;
    this.apiService.UserLiked(postid, this.userid ).subscribe((result: any) => {
      this.likedcount = result.data;
      this.userPost();
      console.log('data saved....');
     });
  }

  search(event: any): void{
    console.log(event.target.value);
    this.apiService.AllUsers(event.target.value, this.userid).subscribe((result: any) => {
      this.userslist = result.data;
      console.log('users list ===>', this.userslist);
     });
  }

  friendRequest(receiverid): void{
    this.apiService.FriendReq(receiverid, this.userid).subscribe((result: any) => {
      this.userslist = result.data;
      console.log('users list ===>', this.userslist);
     });

  }

  friendAccept(): void{
    this.apiService.FriendAccept(this.userid).subscribe((result: any) => {
      this.acceptlist = result.data;
      console.log('users list accept ===>', this.acceptlist);
     });

  }
  flagcheck(): void{
    this.acceptlistFlag = true;
  }

  friendAccepts(acceptid): void{
    this.apiService.Accepted(acceptid, this.userid).subscribe((result: any) => {
      this.acceptlist = result.data;
      console.log('users list accept ===>', this.acceptlist);
     });
  }
  logouts(): void{
    // this.router.navigate(['/']);
    this.apiService.Logout().subscribe((result: any) => {
        this.router.navigate(['/']);
     });


  }

  shareFriends(): void{
    this.apiService.GetFriends(this.userid).subscribe((result: any) => {
      this.sharefriends = result.data;
      console.log('users shareFriends ===>', this.sharefriends);
     });
  }
  userInformation(): void{
    this.apiService.userInfo(this.userid).subscribe((result: any) => {
      this.userdata = result.data;
      console.log('login userdata ===>', this.userdata);
     });

  }

  selectFile(event): void {
    // tslint:disable-next-line:prefer-for-of
    for (let i = 0; i < event.target.files.length; i++) {
      this.myFiles.push(event.target.files[i]);
  }
  }
  postdata(): void{

    const formData = new FormData();
    // tslint:disable-next-line:prefer-for-of
    for (let i = 0; i < this.myFiles.length; i++) {
      formData.append('file', this.myFiles[i]);
    }
    formData.append('usertext', this.usertext);
    formData.append('userid', this.userid);
    this.apiService.UserPosts(formData).subscribe((result: any) => {
      console.log('user posted successfully ===>', formData);
     });
    this.usertext = '';
    this.userPost();
  }
}






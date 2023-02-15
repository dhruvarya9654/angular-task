import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-task',
  templateUrl: './task.component.html',
  styleUrls: ['./task.component.css']
})
export class TaskComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  callTask() {
    fetch('http://127.0.0.1:8000/task/')
      .then((response) => {
        return response.text();
      })
      .then((text)=>{
        alert(text);
      })
      .catch((e)=>{
        console.log(e);
      });
  }

}

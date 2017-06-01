# js相关

### 带前缀框的表单
```form
<div class="form-group">
    <div class="input-group">
        <span class="input-group-addon">密码</span>
          <input name="Password" type="Password" class="form-control" placeholder="Password">
    </div> 
</div>
```

### checkbox全选
```html
<script>
 function selectall() 
   { 
     var a = document.getElementsByTagName("input"); 
     for (var i=0; i<a.length; i++) 
        if (a[i].type == "checkbox") a[i].checked =!a[i].checked; 
    } 
</script>

<form id="form" name="form" method="post" action=""> 
  <input type="checkbox" name="sid" value="1" /> 
  <input name="thes" type="button" onclick="javascript:selectall()" value="全选" /> 
</form> 
```

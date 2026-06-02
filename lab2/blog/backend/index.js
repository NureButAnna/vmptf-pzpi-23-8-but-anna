import express from 'express';
import cors from 'cors';
import multer from 'multer';
import mongoose from 'mongoose';
 
import { registerValidator, loginValidator } from './validations/auth.js';
import { postCreateValidation } from './validations/post.js';
import { checkAuth, handleValidationErrors } from './utils/index.js';
import { UserController, PostController, CommentController } from './controllers/index.js';
 
const app = express();
 
app.use(cors({
  origin: 'http://localhost:5173',
}));
 
app.use(express.json());
 
mongoose.connect(
  'mongodb+srv://ann_db_user:zQ3VHZkWocSUuu9X@blog-cluster.1nsnazh.mongodb.net/blog-db?appName=blog-cluster'
)
.then(() => console.log('DB OK'))
.catch((err) => console.log('DB error', err));
 
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'uploads');
  },
  filename: (req, file, cb) => {
    cb(null, Date.now() + '-' + file.originalname);
  },
});
 
const upload = multer({ storage });
 
app.use('/uploads', express.static('uploads'));
 
const host = '127.0.0.1';
const port = 7000;
 
app.get('/', (req, res) => {
  res.send('Hello World!');
});
 
app.get('/me', checkAuth, UserController.getMe);
app.post('/login', loginValidator, handleValidationErrors, UserController.login);
app.post('/register', registerValidator, handleValidationErrors, UserController.register);
 
app.post('/upload', checkAuth, upload.single('image'), (req, res) => {
  res.json({
    url: `/uploads/${req.file.originalname}`,
  });
});
 
app.get('/posts', PostController.getAll);
app.get('/posts/:id', PostController.getOne);
app.post('/posts', checkAuth, postCreateValidation, PostController.create);
app.delete('/posts/:id', checkAuth, PostController.remove);
app.patch('/posts/:id', checkAuth, PostController.update);

app.get('/comments', CommentController.getAll);
app.get('/comments/:id', CommentController.getOne);
app.post('/comments', checkAuth, postCreateValidation,CommentController.create);
app.delete('/comments/:id', checkAuth, CommentController.remove);
 
app.listen(port, host, (err) => {
  if (err) return console.log(err);
  console.log(`Server listens http://${host}:${port}`);
});
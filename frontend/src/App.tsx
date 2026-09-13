import { Navigate, Outlet, Route, Routes } from "react-router-dom";
import { BrandMark } from "./components/BrandMark";
import { ConsentBanner } from "./components/ConsentBanner";
import { Layout } from "./components/Layout";
import { useAuth } from "./context/AuthContext";
import { ExamPage, ExamsPage, TestPage } from "./pages/AssessmentPages";
import { Dashboard } from "./pages/Dashboard";
import { GrammarLevels, ModuleList } from "./pages/Grammar";
import { Landing } from "./pages/Landing";
import { LessonPage } from "./pages/LessonPage";
import { Login } from "./pages/Login";
import { ModuleHub } from "./pages/ModuleHub";
import { PracticePage } from "./pages/PracticePage";
import { Profile } from "./pages/Profile";
import { PrivacyPage, TermsPage } from "./pages/LegalPages";
import { Register } from "./pages/Register";
import { CheckEmail, VerifyEmail } from "./pages/VerifyEmail";
import { PhoneticsPage, PhoneticsTopicPage } from "./pages/PhoneticsPages";
import { VocabPage, VocabTopicPage } from "./pages/VocabPages";
import { StudyDeckPage, StudyHub } from "./pages/StudyPages";
import {
  AdminDashboard,
  AdminDonation,
  AdminExamDetail,
  AdminExams,
  AdminLayout,
  AdminModuleContent,
  AdminModules,
  AdminUsers,
  AdminVocab,
  AdminVocabTopic,
} from "./pages/admin/AdminPages";

function GuestOnly() {
  const { user, loading } = useAuth();
  if (loading) return <Splash />;
  if (user) return <Navigate to={user.role === "admin" ? "/admin" : "/app"} replace />;
  return <Outlet />;
}

function RequireAuth() {
  const { user, loading } = useAuth();
  if (loading) return <Splash />;
  if (!user) return <Navigate to="/login" replace />;
  return <Outlet />;
}

function RequireAdmin() {
  const { user, loading } = useAuth();
  if (loading) return <Splash />;
  if (!user) return <Navigate to="/login" replace />;
  if (user.role !== "admin") return <Navigate to="/app" replace />;
  return <Outlet />;
}

function Splash() {
  return (
    <div className="surface-grid grid min-h-screen place-items-center">
      <BrandMark size="lg" />
    </div>
  );
}

export function App() {
  return (
    <>
      <ConsentBanner />
      <Routes>
        <Route path="/terms" element={<TermsPage />} />
        <Route path="/privacy" element={<PrivacyPage />} />
        <Route element={<GuestOnly />}>
          <Route path="/" element={<Landing />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/check-email" element={<CheckEmail />} />
        </Route>
        <Route path="/verify" element={<VerifyEmail />} />
        <Route element={<RequireAuth />}>
          <Route path="/app" element={<Layout />}>
            <Route index element={<Dashboard />} />
            <Route path="grammar" element={<GrammarLevels />} />
            <Route path="grammar/:code" element={<ModuleList />} />
            <Route path="module/:slug" element={<ModuleHub />} />
            <Route path="module/:slug/lesson/:lessonId" element={<LessonPage />} />
            <Route path="module/:slug/practice" element={<PracticePage />} />
            <Route path="module/:slug/test" element={<TestPage />} />
            <Route path="exams" element={<ExamsPage />} />
            <Route path="exams/:examId" element={<ExamPage />} />
            <Route path="sounds" element={<PhoneticsPage />} />
            <Route path="sounds/:slug" element={<PhoneticsTopicPage />} />
            <Route path="vocab" element={<VocabPage />} />
            <Route path="vocab/:slug" element={<VocabTopicPage />} />
            <Route path="verbs" element={<StudyHub kind="verbs" />} />
            <Route path="verbs/:slug" element={<StudyDeckPage kind="verbs" />} />
            <Route path="idioms" element={<StudyHub kind="idioms" />} />
            <Route path="idioms/:slug" element={<StudyDeckPage kind="idioms" />} />
            <Route path="exceptions" element={<StudyHub kind="exceptions" />} />
            <Route path="exceptions/:slug" element={<StudyDeckPage kind="exceptions" />} />
            <Route path="profile" element={<Profile />} />
          </Route>
        </Route>
        <Route element={<RequireAdmin />}>
          <Route path="/admin" element={<AdminLayout />}>
            <Route index element={<AdminDashboard />} />
            <Route path="users" element={<AdminUsers />} />
            <Route path="modules" element={<AdminModules />} />
            <Route path="modules/:moduleId" element={<AdminModuleContent />} />
            <Route path="vocab" element={<AdminVocab />} />
            <Route path="vocab/:topicId" element={<AdminVocabTopic />} />
            <Route path="exams" element={<AdminExams />} />
            <Route path="exams/:examId" element={<AdminExamDetail />} />
            <Route path="donation" element={<AdminDonation />} />
          </Route>
        </Route>
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </>
  );
}

/********************************************************************************
** Form generated from reading UI file 'VMSettings_ui.ui'
**
** Created by: Qt User Interface Compiler version 5.12.9
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef VMSETTINGS_UI_H
#define VMSETTINGS_UI_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStackedWidget>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_VmSettings_ui
{
public:
    QGridLayout *gridLayout;
    QLabel *label;
    QPushButton *generalButton;
    QPushButton *isoButton;
    QPushButton *hardwareButton;
    QPushButton *userButton;
    QPushButton *proxiesButton;
    QStackedWidget *stackedWidget;
    QWidget *page;
    QLabel *label_2;
    QLabel *label_3;
    QLineEdit *leComment;
    QLineEdit *leVmName;
    QCheckBox *chkVmware;
    QCheckBox *chkVbox;
    QCheckBox *chkParallels;
    QCheckBox *chkDesktop;
    QCheckBox *chkUpdate;
    QCheckBox *chkVagrant;
    QWidget *page_3;
    QLabel *label_4;
    QLabel *label_5;
    QLabel *label_6;
    QLabel *label_7;
    QLineEdit *leIsoName;
    QLineEdit *leIsoUrl;
    QLineEdit *leIsoHash;
    QLineEdit *leIsoPath;
    QLabel *label_11;
    QLineEdit *leIsoHashAlgorithm;
    QWidget *page_4;
    QLabel *label_8;
    QLabel *label_9;
    QLabel *label_10;
    QLineEdit *leCpus;
    QLineEdit *leMemSize;
    QLineEdit *leDiskSize;
    QWidget *page_5;
    QLineEdit *leUserName;
    QLineEdit *leUserPassword;
    QLineEdit *leVerifyPassword;
    QLineEdit *leUserHomeDir;
    QLineEdit *leUserShell;
    QLabel *laUserName;
    QLabel *laUserPassword;
    QLabel *laVerifyPassword;
    QLabel *laUserHomeDir;
    QLabel *laUserShell;
    QLabel *laUserComment;
    QLineEdit *leUserComment;
    QWidget *page_6;
    QLabel *laHttp_proxy;
    QLabel *laHttps_proxy;
    QLabel *laFtpProxy;
    QLabel *laRsyncProxy;
    QLineEdit *leHttpProxy;
    QLineEdit *leHttpsProxy;
    QLineEdit *leFtpProxy;
    QLineEdit *leRsyncProxy;
    QLabel *laNoProxy;
    QLineEdit *leNoProxy;
    QWidget *page_2;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *VmSettings_ui)
    {
        if (VmSettings_ui->objectName().isEmpty())
            VmSettings_ui->setObjectName(QString::fromUtf8("VmSettings_ui"));
        VmSettings_ui->resize(620, 400);
        gridLayout = new QGridLayout(VmSettings_ui);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        label = new QLabel(VmSettings_ui);
        label->setObjectName(QString::fromUtf8("label"));
        QFont font;
        font.setPointSize(24);
        label->setFont(font);

        gridLayout->addWidget(label, 0, 0, 1, 3);

        generalButton = new QPushButton(VmSettings_ui);
        generalButton->setObjectName(QString::fromUtf8("generalButton"));

        gridLayout->addWidget(generalButton, 1, 0, 1, 1);

        isoButton = new QPushButton(VmSettings_ui);
        isoButton->setObjectName(QString::fromUtf8("isoButton"));

        gridLayout->addWidget(isoButton, 1, 1, 1, 1);

        hardwareButton = new QPushButton(VmSettings_ui);
        hardwareButton->setObjectName(QString::fromUtf8("hardwareButton"));

        gridLayout->addWidget(hardwareButton, 1, 2, 1, 1);

        userButton = new QPushButton(VmSettings_ui);
        userButton->setObjectName(QString::fromUtf8("userButton"));

        gridLayout->addWidget(userButton, 1, 3, 1, 1);

        proxiesButton = new QPushButton(VmSettings_ui);
        proxiesButton->setObjectName(QString::fromUtf8("proxiesButton"));

        gridLayout->addWidget(proxiesButton, 1, 4, 1, 1);

        stackedWidget = new QStackedWidget(VmSettings_ui);
        stackedWidget->setObjectName(QString::fromUtf8("stackedWidget"));
        page = new QWidget();
        page->setObjectName(QString::fromUtf8("page"));
        label_2 = new QLabel(page);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(20, 20, 61, 16));
        label_3 = new QLabel(page);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setGeometry(QRect(20, 60, 71, 16));
        leComment = new QLineEdit(page);
        leComment->setObjectName(QString::fromUtf8("leComment"));
        leComment->setGeometry(QRect(100, 20, 341, 21));
        leVmName = new QLineEdit(page);
        leVmName->setObjectName(QString::fromUtf8("leVmName"));
        leVmName->setGeometry(QRect(100, 60, 341, 21));
        chkVmware = new QCheckBox(page);
        chkVmware->setObjectName(QString::fromUtf8("chkVmware"));
        chkVmware->setGeometry(QRect(20, 100, 86, 20));
        chkVbox = new QCheckBox(page);
        chkVbox->setObjectName(QString::fromUtf8("chkVbox"));
        chkVbox->setGeometry(QRect(20, 130, 86, 20));
        chkParallels = new QCheckBox(page);
        chkParallels->setObjectName(QString::fromUtf8("chkParallels"));
        chkParallels->setGeometry(QRect(20, 160, 86, 20));
        chkDesktop = new QCheckBox(page);
        chkDesktop->setObjectName(QString::fromUtf8("chkDesktop"));
        chkDesktop->setGeometry(QRect(290, 100, 86, 20));
        chkUpdate = new QCheckBox(page);
        chkUpdate->setObjectName(QString::fromUtf8("chkUpdate"));
        chkUpdate->setGeometry(QRect(430, 100, 86, 20));
        chkVagrant = new QCheckBox(page);
        chkVagrant->setObjectName(QString::fromUtf8("chkVagrant"));
        chkVagrant->setGeometry(QRect(20, 190, 86, 16));
        stackedWidget->addWidget(page);
        page_3 = new QWidget();
        page_3->setObjectName(QString::fromUtf8("page_3"));
        label_4 = new QLabel(page_3);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setGeometry(QRect(30, 20, 59, 16));
        label_5 = new QLabel(page_3);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setGeometry(QRect(30, 50, 59, 16));
        label_6 = new QLabel(page_3);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        label_6->setGeometry(QRect(30, 110, 59, 16));
        label_7 = new QLabel(page_3);
        label_7->setObjectName(QString::fromUtf8("label_7"));
        label_7->setGeometry(QRect(30, 140, 131, 16));
        leIsoName = new QLineEdit(page_3);
        leIsoName->setObjectName(QString::fromUtf8("leIsoName"));
        leIsoName->setGeometry(QRect(100, 20, 411, 21));
        leIsoUrl = new QLineEdit(page_3);
        leIsoUrl->setObjectName(QString::fromUtf8("leIsoUrl"));
        leIsoUrl->setGeometry(QRect(100, 50, 411, 21));
        leIsoHash = new QLineEdit(page_3);
        leIsoHash->setObjectName(QString::fromUtf8("leIsoHash"));
        leIsoHash->setGeometry(QRect(100, 110, 411, 21));
        leIsoPath = new QLineEdit(page_3);
        leIsoPath->setObjectName(QString::fromUtf8("leIsoPath"));
        leIsoPath->setGeometry(QRect(100, 80, 411, 21));
        label_11 = new QLabel(page_3);
        label_11->setObjectName(QString::fromUtf8("label_11"));
        label_11->setGeometry(QRect(30, 80, 59, 16));
        leIsoHashAlgorithm = new QLineEdit(page_3);
        leIsoHashAlgorithm->setObjectName(QString::fromUtf8("leIsoHashAlgorithm"));
        leIsoHashAlgorithm->setGeometry(QRect(160, 140, 351, 21));
        stackedWidget->addWidget(page_3);
        page_4 = new QWidget();
        page_4->setObjectName(QString::fromUtf8("page_4"));
        label_8 = new QLabel(page_4);
        label_8->setObjectName(QString::fromUtf8("label_8"));
        label_8->setGeometry(QRect(10, 10, 91, 16));
        label_9 = new QLabel(page_4);
        label_9->setObjectName(QString::fromUtf8("label_9"));
        label_9->setGeometry(QRect(10, 40, 91, 16));
        label_10 = new QLabel(page_4);
        label_10->setObjectName(QString::fromUtf8("label_10"));
        label_10->setGeometry(QRect(10, 70, 91, 16));
        leCpus = new QLineEdit(page_4);
        leCpus->setObjectName(QString::fromUtf8("leCpus"));
        leCpus->setGeometry(QRect(110, 10, 113, 21));
        leMemSize = new QLineEdit(page_4);
        leMemSize->setObjectName(QString::fromUtf8("leMemSize"));
        leMemSize->setGeometry(QRect(110, 40, 113, 21));
        leDiskSize = new QLineEdit(page_4);
        leDiskSize->setObjectName(QString::fromUtf8("leDiskSize"));
        leDiskSize->setGeometry(QRect(110, 70, 113, 21));
        stackedWidget->addWidget(page_4);
        page_5 = new QWidget();
        page_5->setObjectName(QString::fromUtf8("page_5"));
        leUserName = new QLineEdit(page_5);
        leUserName->setObjectName(QString::fromUtf8("leUserName"));
        leUserName->setGeometry(QRect(140, 20, 261, 21));
        leUserPassword = new QLineEdit(page_5);
        leUserPassword->setObjectName(QString::fromUtf8("leUserPassword"));
        leUserPassword->setGeometry(QRect(140, 50, 261, 21));
        leUserPassword->setEchoMode(QLineEdit::Password);
        leVerifyPassword = new QLineEdit(page_5);
        leVerifyPassword->setObjectName(QString::fromUtf8("leVerifyPassword"));
        leVerifyPassword->setGeometry(QRect(140, 80, 261, 21));
        leVerifyPassword->setEchoMode(QLineEdit::Password);
        leUserHomeDir = new QLineEdit(page_5);
        leUserHomeDir->setObjectName(QString::fromUtf8("leUserHomeDir"));
        leUserHomeDir->setGeometry(QRect(140, 150, 261, 21));
        leUserShell = new QLineEdit(page_5);
        leUserShell->setObjectName(QString::fromUtf8("leUserShell"));
        leUserShell->setGeometry(QRect(140, 180, 261, 21));
        laUserName = new QLabel(page_5);
        laUserName->setObjectName(QString::fromUtf8("laUserName"));
        laUserName->setGeometry(QRect(10, 20, 121, 16));
        laUserPassword = new QLabel(page_5);
        laUserPassword->setObjectName(QString::fromUtf8("laUserPassword"));
        laUserPassword->setGeometry(QRect(10, 50, 121, 16));
        laVerifyPassword = new QLabel(page_5);
        laVerifyPassword->setObjectName(QString::fromUtf8("laVerifyPassword"));
        laVerifyPassword->setGeometry(QRect(10, 80, 121, 16));
        laUserHomeDir = new QLabel(page_5);
        laUserHomeDir->setObjectName(QString::fromUtf8("laUserHomeDir"));
        laUserHomeDir->setGeometry(QRect(10, 150, 121, 16));
        laUserShell = new QLabel(page_5);
        laUserShell->setObjectName(QString::fromUtf8("laUserShell"));
        laUserShell->setGeometry(QRect(10, 180, 111, 16));
        laUserComment = new QLabel(page_5);
        laUserComment->setObjectName(QString::fromUtf8("laUserComment"));
        laUserComment->setGeometry(QRect(10, 110, 121, 31));
        laUserComment->setWordWrap(true);
        leUserComment = new QLineEdit(page_5);
        leUserComment->setObjectName(QString::fromUtf8("leUserComment"));
        leUserComment->setGeometry(QRect(140, 110, 261, 21));
        stackedWidget->addWidget(page_5);
        page_6 = new QWidget();
        page_6->setObjectName(QString::fromUtf8("page_6"));
        laHttp_proxy = new QLabel(page_6);
        laHttp_proxy->setObjectName(QString::fromUtf8("laHttp_proxy"));
        laHttp_proxy->setGeometry(QRect(20, 10, 81, 16));
        laHttps_proxy = new QLabel(page_6);
        laHttps_proxy->setObjectName(QString::fromUtf8("laHttps_proxy"));
        laHttps_proxy->setGeometry(QRect(20, 40, 81, 16));
        laFtpProxy = new QLabel(page_6);
        laFtpProxy->setObjectName(QString::fromUtf8("laFtpProxy"));
        laFtpProxy->setGeometry(QRect(20, 70, 81, 16));
        laRsyncProxy = new QLabel(page_6);
        laRsyncProxy->setObjectName(QString::fromUtf8("laRsyncProxy"));
        laRsyncProxy->setGeometry(QRect(20, 100, 81, 16));
        leHttpProxy = new QLineEdit(page_6);
        leHttpProxy->setObjectName(QString::fromUtf8("leHttpProxy"));
        leHttpProxy->setGeometry(QRect(110, 10, 241, 21));
        leHttpsProxy = new QLineEdit(page_6);
        leHttpsProxy->setObjectName(QString::fromUtf8("leHttpsProxy"));
        leHttpsProxy->setGeometry(QRect(110, 40, 241, 21));
        leFtpProxy = new QLineEdit(page_6);
        leFtpProxy->setObjectName(QString::fromUtf8("leFtpProxy"));
        leFtpProxy->setGeometry(QRect(110, 70, 241, 21));
        leRsyncProxy = new QLineEdit(page_6);
        leRsyncProxy->setObjectName(QString::fromUtf8("leRsyncProxy"));
        leRsyncProxy->setGeometry(QRect(110, 100, 241, 21));
        laNoProxy = new QLabel(page_6);
        laNoProxy->setObjectName(QString::fromUtf8("laNoProxy"));
        laNoProxy->setGeometry(QRect(20, 130, 81, 16));
        leNoProxy = new QLineEdit(page_6);
        leNoProxy->setObjectName(QString::fromUtf8("leNoProxy"));
        leNoProxy->setGeometry(QRect(110, 130, 241, 21));
        stackedWidget->addWidget(page_6);
        page_2 = new QWidget();
        page_2->setObjectName(QString::fromUtf8("page_2"));
        stackedWidget->addWidget(page_2);

        gridLayout->addWidget(stackedWidget, 2, 0, 1, 5);

        buttonBox = new QDialogButtonBox(VmSettings_ui);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Apply|QDialogButtonBox::Cancel|QDialogButtonBox::Reset|QDialogButtonBox::Save);

        gridLayout->addWidget(buttonBox, 3, 2, 1, 3);

        QWidget::setTabOrder(generalButton, isoButton);
        QWidget::setTabOrder(isoButton, hardwareButton);
        QWidget::setTabOrder(hardwareButton, userButton);
        QWidget::setTabOrder(userButton, proxiesButton);
        QWidget::setTabOrder(proxiesButton, leComment);
        QWidget::setTabOrder(leComment, leVmName);
        QWidget::setTabOrder(leVmName, leIsoName);
        QWidget::setTabOrder(leIsoName, leIsoUrl);
        QWidget::setTabOrder(leIsoUrl, leIsoHash);
        QWidget::setTabOrder(leIsoHash, leCpus);
        QWidget::setTabOrder(leCpus, leMemSize);
        QWidget::setTabOrder(leMemSize, leDiskSize);
        QWidget::setTabOrder(leDiskSize, leUserName);
        QWidget::setTabOrder(leUserName, leUserPassword);
        QWidget::setTabOrder(leUserPassword, leVerifyPassword);
        QWidget::setTabOrder(leVerifyPassword, leUserComment);
        QWidget::setTabOrder(leUserComment, leUserHomeDir);
        QWidget::setTabOrder(leUserHomeDir, leUserShell);
        QWidget::setTabOrder(leUserShell, leHttpProxy);
        QWidget::setTabOrder(leHttpProxy, leHttpsProxy);
        QWidget::setTabOrder(leHttpsProxy, leFtpProxy);
        QWidget::setTabOrder(leFtpProxy, leRsyncProxy);
        QWidget::setTabOrder(leRsyncProxy, leNoProxy);

        retranslateUi(VmSettings_ui);
        QObject::connect(buttonBox, SIGNAL(accepted()), VmSettings_ui, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), VmSettings_ui, SLOT(reject()));

        stackedWidget->setCurrentIndex(1);


        QMetaObject::connectSlotsByName(VmSettings_ui);
    } // setupUi

    void retranslateUi(QDialog *VmSettings_ui)
    {
        VmSettings_ui->setWindowTitle(QApplication::translate("VmSettings_ui", "Dialog", nullptr));
        label->setText(QApplication::translate("VmSettings_ui", "Virtual Machine Settings", nullptr));
        generalButton->setText(QApplication::translate("VmSettings_ui", "General", nullptr));
        isoButton->setText(QApplication::translate("VmSettings_ui", "ISO", nullptr));
        hardwareButton->setText(QApplication::translate("VmSettings_ui", "Hardware", nullptr));
        userButton->setText(QApplication::translate("VmSettings_ui", "User", nullptr));
        proxiesButton->setText(QApplication::translate("VmSettings_ui", "Proxies", nullptr));
        label_2->setText(QApplication::translate("VmSettings_ui", "Comment", nullptr));
        label_3->setText(QApplication::translate("VmSettings_ui", "VM Name", nullptr));
        chkVmware->setText(QApplication::translate("VmSettings_ui", "VMware", nullptr));
        chkVbox->setText(QApplication::translate("VmSettings_ui", "Virtualbox", nullptr));
        chkParallels->setText(QApplication::translate("VmSettings_ui", "Paralells", nullptr));
        chkDesktop->setText(QApplication::translate("VmSettings_ui", "Desktop", nullptr));
        chkUpdate->setText(QApplication::translate("VmSettings_ui", "Updates", nullptr));
        chkVagrant->setText(QApplication::translate("VmSettings_ui", "Vagrant", nullptr));
        label_4->setText(QApplication::translate("VmSettings_ui", "Iso Name", nullptr));
        label_5->setText(QApplication::translate("VmSettings_ui", "Iso URL", nullptr));
        label_6->setText(QApplication::translate("VmSettings_ui", "Iso Hash", nullptr));
        label_7->setText(QApplication::translate("VmSettings_ui", "ISO Hash Algorithm", nullptr));
        label_11->setText(QApplication::translate("VmSettings_ui", "Iso Path", nullptr));
        label_8->setText(QApplication::translate("VmSettings_ui", "CPUs", nullptr));
        label_9->setText(QApplication::translate("VmSettings_ui", "Memory Size", nullptr));
        label_10->setText(QApplication::translate("VmSettings_ui", "Disk Size", nullptr));
        laUserName->setText(QApplication::translate("VmSettings_ui", "Ssh User Name", nullptr));
        laUserPassword->setText(QApplication::translate("VmSettings_ui", "Ssh User Password", nullptr));
        laVerifyPassword->setText(QApplication::translate("VmSettings_ui", "Verify Password", nullptr));
        laUserHomeDir->setText(QApplication::translate("VmSettings_ui", "User Home Dir", nullptr));
        laUserShell->setText(QApplication::translate("VmSettings_ui", "User Shell", nullptr));
        laUserComment->setText(QApplication::translate("VmSettings_ui", "User Long Name/Comment", nullptr));
        laHttp_proxy->setText(QApplication::translate("VmSettings_ui", "http_proxy", nullptr));
        laHttps_proxy->setText(QApplication::translate("VmSettings_ui", "https_proxy", nullptr));
        laFtpProxy->setText(QApplication::translate("VmSettings_ui", "ftp_proxy", nullptr));
        laRsyncProxy->setText(QApplication::translate("VmSettings_ui", "rsync_proxy", nullptr));
        laNoProxy->setText(QApplication::translate("VmSettings_ui", "no_proxy", nullptr));
    } // retranslateUi

};

namespace Ui {
    class VmSettings_ui: public Ui_VmSettings_ui {};
} // namespace Ui

QT_END_NAMESPACE

#endif // VMSETTINGS_UI_H
